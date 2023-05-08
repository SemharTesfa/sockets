from DatabasePy import Database
from Business import Business
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt;

plt.rcdefaults()


class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


B = Business()
D = Database('SQLite_Python.db', 'Database')

def draw_graph(country):
    B.query_to_database(country)

def create_frame():
    root = tk.Tk()
    frame = ScrollableFrame(root)

    data = D.get_countries()

    for i in range(len(data)):
        ttk.Button(frame.scrollable_frame, text=f"{data[i]}", width=50, command=lambda k=data[i]: draw_graph(k)).pack()

    frame.pack()
    root.mainloop()



