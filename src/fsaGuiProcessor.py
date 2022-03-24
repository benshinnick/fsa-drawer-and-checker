import tkinter as tk

class FsaGuiProcessor:

    STATE_CIR_RAD = 20
    
    def __init__(self, states, num_states, start_state):
        self.states = states
        self.num_states = num_states
        self.start_state = start_state
        self.num_back_transitions_processes = 0

        self.root = tk.Tk()
        self.canvas = self._create_canvas()

    def _create_canvas(self):
        w = self._get_canvas_width()
        h = self._get_canvas_height()
        bg_c = "white"
        return tk.Canvas(self.root, width=w, height=h, borderwidth=0, highlightthickness=0, bg=bg_c)

    def create_and_show_gui(self):
        for i in range(0, self.num_states):
            self.draw_all_state_data(i)
        self.canvas.pack()
        self.root.wm_title("FSA Diagram")
        self.root.mainloop()

    def draw_all_state_data(self, state_num):
        self.draw_all_state_transitions(state_num)
        self.draw_state(state_num)

    def draw_all_state_transitions(self, state_num):
        if self.states[state_num].is_start_state():
            self._draw_start_state_transition(state_num)
        for i in range(0, self.states[state_num].get_num_transitions()):
            curr_transition = self.states[state_num].get_transition(i)
            if curr_transition.is_self_transition():
                self._draw_self_transition(curr_transition)
            elif curr_transition.is_back_transition():
                self._draw_back_transition(curr_transition)
            elif curr_transition.is_forward_transition():
                self._draw_forward_transition(curr_transition)

    def draw_state(self, state_num):
        state_coord = self._get_state_center_coord(state_num)
        x, y = state_coord[0], state_coord[1]
        if self.states[state_num].is_accept_state():
            self._draw_accept_state_cir(x, y)
        else:
            self._draw_state_cir(x, y)
        self._create_text(x, y, state_num)

    def _draw_state_cir(self,x, y):
        self._create_circle(x, y, self.STATE_CIR_RAD)
        self.canvas.pack()

    def _draw_accept_state_cir(self,x,y):
        self._create_circle(x, y, self.STATE_CIR_RAD)
        self._create_circle(x, y, self.STATE_CIR_RAD - 3)
        self.canvas.pack()

    def _draw_start_state_transition(self, state_num):
        state_coord = self._get_state_center_coord(state_num)
        x, y = state_coord[0] - 15, state_coord[1] - 15
        self._create_arrow(x-24, y-25, x, y)

    def _draw_self_transition(self, transition):
        state_coord = self._get_state_center_coord(transition.get_from_state_num())
        x, y = state_coord[0] + 25, state_coord[1]
        self._create_circle(x, y, self.STATE_CIR_RAD)
        self._create_text(x + 27, y, transition.get_char())
        x -= self.STATE_CIR_RAD - 7
        y -= self.STATE_CIR_RAD - 5
        self._create_line(x, y, x+7, y)
        self._create_line(x, y, x, y-7)

    def _draw_back_transition(self, transition):
        from_state_coord = self._get_state_center_coord(transition.get_from_state_num())
        to_state_coord = self._get_state_center_coord(transition.get_to_state_num())
        from_x, from_y = from_state_coord[0] - 25, from_state_coord[1]
        to_x, to_y = to_state_coord[0] - 25, to_state_coord[1]
        back_line_x = to_x - ((self.num_back_transitions_processes + 1) * 30)
        self._create_line(from_x, from_y, back_line_x, from_y)
        self._create_line(back_line_x, from_y, back_line_x, to_y)
        self._create_arrow(back_line_x, to_y, to_x, to_y)
        self._create_text(back_line_x - 7, (from_y+to_y)/2, transition.get_char())

        self.num_back_transitions_processes += 1

    def _draw_forward_transition(self, transition):
        state_coord = self._get_state_center_coord(transition.get_from_state_num())
        x, y = state_coord[0], state_coord[1] + 23
        if(transition.get_to_state_num() == transition.get_from_state_num() + 1):
            self._create_arrow(x, y, x, y + 30)
            self._create_text(x - 8, y + 10, transition.get_char())

    def _create_circle(self, x, y, r):
        x0, y0 = x - r, y - r
        x1, y1 = x + r, y + r
        return self.canvas.create_oval(x0, y0, x1, y1, fill="white", outline="black", width=1)

    def _create_line(self, x1, y1, x2, y2):
        return self.canvas.create_line(x1, y1, x2, y2, width = 1, fill="black")

    def _create_arrow(self, x1, y1, x2, y2):
        return self.canvas.create_line(x1, y1, x2, y2, width = 1, fill="black", arrow=tk.LAST)

    def _create_text(self, x, y, text):
        return self.canvas.create_text(x, y, fill="black", text=str(text))

    def _get_state_center_coord(self, state_num):
        x = self._get_canvas_width() / 2
        y = 50 + (state_num * 75)
        return [x, y]

    def _get_canvas_width(self):
        return 300 + (self._get_num_of_back_transitions() * 35)
    
    def _get_canvas_height(self):
        return 10 + (self.num_states * 75)

    def _get_num_of_back_transitions(self):
        back_total = 0
        for i in range(0,len(self.states)):
            back_total += self.states[i].get_num_of_back_transitions()
        return back_total