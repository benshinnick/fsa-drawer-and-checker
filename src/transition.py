class Transition:

    def __init__(self, fromStateNum, toStateNum, character):
        self.fromStateNum = int(fromStateNum)
        self.toStateNum = int(toStateNum)
        self.character = character

    def get_char(self):
        return self.character
    
    def get_to_state_num(self):
        return self.toStateNum

    def get_from_state_num(self):
        return self.fromStateNum

    def is_self_transition(self):
        return self.toStateNum == self.fromStateNum
    
    def is_forward_transition(self):
        return self.toStateNum > self.fromStateNum

    def is_back_transition(self):
        return self.toStateNum < self.fromStateNum

    def __str__(self):
        return "(" + str(self.fromStateNum) + ":" + str(self.toStateNum) + ":" + str(self.character) + ")" 