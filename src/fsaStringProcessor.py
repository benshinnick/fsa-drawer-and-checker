class FsaStringProcessor:
    
    def __init__(self, string, states, num_states):
        self.string = string
        self.states = states
        self.num_states = num_states

    def is_legal_str(self):
        return True

