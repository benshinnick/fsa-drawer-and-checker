import sys

from .fsaStringProcessor import FsaStringProcessor
from .fsaGuiProcessor import FsaGuiProcessor
from .state import State
from .transition import Transition

class FiniteStateAutomata:

    def __init__(self, def_file_name):
        tokens = self._get_tokens_from_def_file(def_file_name)
        self.num_states = int(tokens[0])
        self.start_state = int(tokens[3])
        self.states = self._create_states_from_tokens(tokens)

    def _get_tokens_from_def_file(self, def_file_name):
        with open(def_file_name) as fsa_file:
            content = fsa_file.readline()
        tokens = content.split(';')
        return tokens

    def _create_states_from_tokens(self, tokens):
        transitionData = tokens[2].split(',')
        acceptStates = tokens[4].split(',')
        transitions = self._create_transitions_from_tansition_data(transitionData)

        states = []
        for i in range(0,self.num_states):
            states.append(State(i))
            for j in range(0, len(transitions)):
                if transitions[j].get_from_state_num() == i:
                    states[i].add_transition(transitions[j])
        states[self.start_state].set_is_start(True)
        for i in range(0, len(acceptStates)):
            states[int(acceptStates[i])].set_is_accept(True)
        return states

    def _create_transitions_from_tansition_data(self, transitionData):
        transitions = []
        for i in range(0, len(transitionData)):
            from_state_num = transitionData[i][1]
            to_state_num = transitionData[i][3]
            character = transitionData[i][5]
            transitions.append(Transition(from_state_num, to_state_num, character))
        return transitions

    def show_states(self):
        print("States:")
        for i in range(0,len(self.states)):
            print(str(self.states[i]))

    def process_string(self, str_file_name):
        with open(str_file_name) as str_file:
            string = str_file.readline()
        print('Processing: \'' + string + '\'')
        is_legal_str = self.check_string(string)
        if is_legal_str: print('Success: \'' + string + '\' is legal')
        else: print('Failure: \'' + string + '\' is not legal')

    def check_string(self, string):
        str_processor = FsaStringProcessor(string, self.states, self.num_states, self.start_state)
        return str_processor.is_legal_str()

    def process_gui(self):
        gui_processor = FsaGuiProcessor(self.states, self.num_states, self.start_state)
        gui_processor.create_and_show_gui()

fsa_def_file_name = sys.argv[1]
fsa_str_file_name = sys.argv[2]

fsa = FiniteStateAutomata(fsa_def_file_name)
# fsa.show_states()
fsa.process_string(fsa_str_file_name)
fsa.process_gui()