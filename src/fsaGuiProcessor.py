import tkinter as tk

class FsaGuiProcessor:
    
    def __init__(self, states, num_states, start_state):
        self.states = states
        self.num_states = num_states
        self.start_state = start_state
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=300, height=500, borderwidth=0, highlightthickness=0)

    def create_and_show_gui(self):
        self.canvas.create_line(40, 75, 40, 200, width = 2, arrow=tk.LAST)
        cir = self.canvas.create_oval(10, 50, 70, 110, fill="red")
        coord = 10, 200, 70, 260
        cir = self.canvas.create_oval(coord, fill="red")
        self.canvas.create_text(50, 145, text='a') 
        self.canvas.pack()
        self.root.wm_title("Circles, lines, and Arcs")
        self.root.mainloop()