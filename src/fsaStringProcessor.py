class FsaStringProcessor:
    
    def __init__(self, string, states, num_states, start_state):
        self.string = string
        self.states = states
        self.num_states = num_states
        self.curr_state = start_state
        self.curr_char_counter = 0

    def is_legal_str(self):
        return True

    def process_next_char(self):
        pass

