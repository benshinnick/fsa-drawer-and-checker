class FsaStringProcessor:
    
    def __init__(self, string, states, num_states, start_state):
        self.string = string
        self.states = states
        self.num_states = num_states
        self.curr_state_num = start_state
        self.curr_char_idx = 0

    def is_legal_str(self):
        num_chars = len(self.string)
        for i in range(0,num_chars - 1):
            print("On state", self.curr_state_num, "Next char", self.string[self.curr_char_idx + 1])
            if not self.is_legal_next_char(): return False
            self.update_curr_state()
            self.update_curr_char()
        if not self.is_curr_state_accept_state(): return False
        return True

    def is_legal_next_char(self):
        next_char = self.string[self.curr_char_idx + 1]
        return self.states[self.curr_state_num].is_legal_transition(next_char)
    
    def update_curr_state(self):
        next_char = self.string[self.curr_char_idx + 1]
        next_state = self.states[self.curr_state_num].get_next_state(next_char)
        self.curr_state_num = next_state

    def update_curr_char(self):
        self.curr_char_idx += 1

    def is_curr_state_accept_state(self):
        return self.states[self.curr_state_num].is_accept_state()

    # 12345


