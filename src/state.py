from operator import truediv


class State:  

    def __init__(self, num):
        self.num = int(num)
        self.transitions = []
        self.is_start = False
        self.is_accept = False

    def is_legal_transition(self, char):
        for i in range(0,len(self.transitions)):
            if(self.transitions[i].get_char == char): return True
        return False

    def next_state(self, char):
        if not self.is_legal_transition(char): return -1
        for i in range(0,len(self.transitions)):
            if(self.transitions[i].get_char == char):
                return self.transitions[i].get_to_state_num()
    
    def addTransition(self, transition):
        self.transitions.append(transition)

    def set_is_start(self, is_start):
        self.is_start = is_start

    def set_state_num(self, num):
        self.num = num

    def get_state_num(self):
        return self.num

    def is_start(self):
        return self.is_start

    def set_is_accept(self, is_accept):
        self.is_accept = is_accept

    def is_accept(self):
        return self.is_accept

    def __str__(self):
        stateStr = "num = " + str(self.num)
        if(self.is_start): stateStr += " [is_start]"
        if(self.is_accept): stateStr += " [is_accept]"
        stateStr += " transitions = "
        for i in range(0,len(self.transitions)):
            stateStr += "[" + str(self.transitions[i]) + "]"
        return stateStr
