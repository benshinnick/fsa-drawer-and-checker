import sys

from fsaStringProcessor import FsaStringProcessor
from fsaGuiProcessor import FsaGuiProcessor
from state import State
from transition import Transition

class FiniteStateAutomata:

    def __init__(self, def_file_name):
        tokens = self._get_tokens_from_def_file(def_file_name)
        self.show_tokens(tokens)
        self.states = self._create_states_from_tokens(tokens)

    def _get_tokens_from_def_file(self, def_file_name):
        with open(def_file_name) as fsa_file:
            content = fsa_file.readline()
        tokens = content.split(';')
        return tokens

    def _create_states_from_tokens(self, tokens):
        numStates = int(tokens[0])
        transitionData = tokens[2].split(',')
        startState = int(tokens[3])
        acceptStates = tokens[4].split(',')
        transitions = self._create_transitions_from_tansition_data(transitionData)

        states = []
        for i in range(0,numStates):
            states.append(State(i))
            for j in range(0, len(transitions)):
                if transitions[j].get_from_state_num() == i:
                    states[i].addTransition(transitions[j])
        states[startState].set_to_start()
        for i in range(0, len(acceptStates)):
            states[int(acceptStates[i])].set_to_accept()
        return states

    def _create_transitions_from_tansition_data(self, transitionData):
        transitions = []
        for i in range(0, len(transitionData)):
            fromStateNum = transitionData[i][1]
            toStateNum = transitionData[i][3]
            character = transitionData[i][5]
            transitions.append(Transition(fromStateNum, toStateNum, character))
        return transitions

    def show_states(self):
        for i in range(0,len(self.states)):
            print(str(self.states[i]))

    def process_string(self):
        strProcessor = FsaStringProcessor()
        pass

    # temporary testing function
    def show_tokens(self, tokens):
        for i in range(0,len(tokens)-1):
            print('token - ' + tokens[i])

fsa_def_file_name = sys.argv[1]
fsa_string_file_name = sys.argv[2]

fsa = FiniteStateAutomata(fsa_def_file_name)
fsa.show_states()