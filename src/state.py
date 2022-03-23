class State:  

    def __init__(self, num):
        self.num = int(num)
        self.transitions = []
        self.is_start = False
        self.is_accept = False

    def set_to_accept(self):
        self.is_accept = True

    def is_accept(self):
        return self.is_accept

    def set_to_start(self):
        self.is_start = True
    
    def addTransition(self, transition):
        self.transitions.append(transition)

    def get_state_num(self):
        return self.num

    def __str__(self):
        stateStr = "num = " + str(self.num) + " is start = " + str(self.is_start) + " is accept = " + str(self.is_accept)
        stateStr += " transitions = "
        for i in range(0,len(self.transitions)):
            stateStr += "[" + str(self.transitions[i]) + "],"
        return stateStr
