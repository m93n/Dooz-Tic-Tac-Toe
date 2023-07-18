from tkinter import *
from tkinter import ttk

root = Tk()
# root.title("DOOOOOOOOOZ")
root.title("دوووووووووز")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

def start():
    root.destroy()
    import datapage
    

# hello_label = ttk.Label(mainframe, text="Hi, wellcome to *** DOOZ *** game", font=("Times bold", 14))
hello_label = ttk.Label(mainframe, text="سلام به **دوز** خوش امدید", font=("Helvetica", 30))

hello_label.grid(column=1, row=1, sticky=W)

ttk.Button(mainframe, text="Start", command=start).grid(column=1, row=2, sticky=S)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=50, pady=30)

root.mainloop()