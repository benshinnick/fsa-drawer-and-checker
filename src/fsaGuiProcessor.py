import tkinter as tk

class FsaGuiProcessor:
    
    def __init__(self, states, num_states, start_state):
        self.states = states
        self.num_states = num_states
        self.start_state = start_state

        self.root = tk.Tk()
        self.canvas = self._create_canvas()

    def _create_canvas(self):
        w = 300 + (self.get_num_of_back_transitions() * 35)
        h = 100 + (self.num_states * 125)
        bg_c = "white"
        return tk.Canvas(self.root, width=w, height=h, borderwidth=0, highlightthickness=0, bg=bg_c)

    def create_and_show_gui(self):
        # self.canvas.create_line(40, 75, 40, 200, width = 2, fill="black", arrow=tk.LAST)
        # cir = self.canvas.create_oval(10, 50, 70, 110, fill="red")
        # coord = 10, 200, 70, 260
        # cir = self.canvas.create_oval(coord, fill="red")
        # self.canvas.create_text(50, 145, fill="black", text='a')
        self.canvas.pack()
        self.root.wm_title("FSA Diagram")
        self.root.mainloop()

    def get_num_of_back_transitions(self):
        back_total = 0
        for i in range(0,len(self.states)):
            back_total += self.states[i].get_num_of_back_transitions()
        return back_total