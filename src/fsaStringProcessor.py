class FsaStringProcessor:
    
    def __init__(self, string, states, num_states, start_state):
        self.string = string
        self.states = states
        self.num_states = num_states
        self.curr_state_num = start_state
        self.curr_char_counter = 0

    def is_legal_str(self):
        num_chars = len(self.string)
        for i in range(0,num_chars - 2):
            if not self.is_legal_next_char(): return False
            self.update_curr_state()
            self.update_curr_char()
        if not self.is_curr_state_accept_state(): return False
        return True

    def is_legal_next_char(self):
        pass

    def update_curr_char(self):
        pass

    def update_curr_state(self):
        pass

    def is_curr_state_accept_state(self):
        return 

    # 12345


