from tkinter import *
from tkinter import ttk
import json

root = Tk()
# root.title("DOOOOOOOOOZ")
root.title("دوووووووووز")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


def submit(*args):
    data = {'first player name':first_player_name.get(), 
            'second player name':second_player_name.get(), 
            'first player char':first_player_character.get(), 
            'second player char':second_player_character.get(), 
            }
    
        
    with open('dooz_data.txt', 'w') as myfile:
        myfile.write(json.dumps(data))
        
    destroy()

def destroy():
    root.destroy()
    import Dooz


first_player_name = StringVar()
first_palayer_name_entry = ttk.Entry(mainframe, width=7, textvariable=first_player_name)
first_palayer_name_entry.grid(column=1, row=2, sticky=(W, E))


second_player_name = StringVar()
second_palayer_name_entry = ttk.Entry(mainframe, width=7, textvariable=second_player_name)
second_palayer_name_entry.grid(column=3, row=2, sticky=(W, E))

first_player_character = StringVar()
first_player_char_entry = ttk.Entry(mainframe, width=1, textvariable=first_player_character,)
first_player_char_entry.grid(column=1, row=4, sticky=(W, E))


second_player_character = StringVar()
second_player_char_entry = ttk.Entry(mainframe, width=1, textvariable=second_player_character)
second_player_char_entry.grid(column=3, row=4, sticky=(W, E))


ttk.Label(mainframe, text='first player name', font=("Helvetica", 15)).grid(column=1, row=1, sticky=(W, E))
ttk.Label(mainframe, text='second player name', font=("Helvetica", 15)).grid(column=3, row=1, sticky=(W, E))

ttk.Label(mainframe, text='first player character', font=("Helvetica", 15)).grid(column=1, row=3, sticky=(W, E))
ttk.Label(mainframe, text='second player character', font=("Helvetica", 15)).grid(column=3, row=3, sticky=(W, E))


ttk.Button(mainframe, text="Submit", command=submit).grid(column=2, row=5, sticky=S, padx=50, pady=50)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

first_palayer_name_entry.focus()
root.bind("<Return>", submit)
 

root.mainloop()