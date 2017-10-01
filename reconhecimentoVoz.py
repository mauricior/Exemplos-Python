from tkinter import *
from tkinter import ttk 




root = Tk()
root.title("Voice Recognition")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)


text_entry = ttk.Entry(mainframe, width=7)
text_entry.grid(column=2, row=1, sticky=(W,E))




root.mainloop()