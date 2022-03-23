class State:  

    def __init__(self, num):
        self.num = num
        self.transitions = []
        self.is_start = False

    def set_to_start(self):
        self.is_start = True