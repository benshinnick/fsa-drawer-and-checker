class Transition:

    def __init__(self, toStateNum, character):
        self.toStateNum = toStateNum
        self.character = character
        self.is_accept = False

    def set_to_accept(self):
        self.is_accept = True

    def is_accept(self):
        return self.is_accept

    def get_char(self):
        return self.character
    
    def get_to_state_num(self):
        return self.toStateNum

    