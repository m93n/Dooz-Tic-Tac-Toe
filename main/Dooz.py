#importing Packages from tkinter
from tkinter import *
from tkinter import messagebox, ttk
import json


with open('dooz_data.txt', 'r') as myfile:
    data = json.loads(myfile.readline())

first_player_name = data['first player name']
second_player_name = data['second player name']
first_player_character = data['first player char']
second_player_character = data['second player char']


Player1 = first_player_character
stop_game = False

def clicked(r,c):
	
	#player
	global Player1
	# global stop_game

	if Player1 == first_player_character and states[r][c] == 0 and stop_game == False:
		b[r][c].configure(text = first_player_character)
		states[r][c] = first_player_character
		Player1=second_player_character

	
	if Player1 == second_player_character and states[r][c] == 0 and stop_game == False:
		b[r][c].configure(text = second_player_character)
		states[r][c] = second_player_character
		Player1 = first_player_character

	check_if_win()

def check_if_win():
	global stop_game

	for i in range(3):
		if states[i][0] == states[i][1] == states[i][2] !=0:
			stop_game = True
   
			if states[i][0] == first_player_character:
				winner_name = first_player_name
			else:
				winner_name = second_player_name
    
			winner = messagebox.showinfo("Winner", winner_name + " Won")
			break

	# for j in range(3):
		elif states[0][i] == states[1][i] == states[2][i] != 0:
			stop_game = True

			if states[0][i] == first_player_character:
				winner_name = first_player_name
			else:
				winner_name = second_player_name

			winner = messagebox.showinfo("Winner", winner_name+ " Won!")
			break

		elif states[0][0] == states[1][1] == states[2][2] !=0:
			stop_game = True

			if states[0][0] == first_player_character:
				winner_name = first_player_name
			else:
				winner_name = second_player_name
   
			winner = messagebox.showinfo("Winner", winner_name+ " Won!")
			break

		elif states[0][2] == states[1][1] == states[2][0] !=0:
			stop_game = True

			if states[0][2] == first_player_character:
				winner_name = first_player_name
			else:
				winner_name = second_player_name

			winner = messagebox.showinfo("Winner" , winner_name+ " Won!")
			break

		elif states[0][0] and states[0][1] and states[0][2] and states[1][0] and states[1][1] and states[1][2] and states[2][0] and states[2][1] and states[2][2] != 0:
			stop_game = True

			winner = messagebox.showinfo("tie", "Tie")

# Design window
#Creating the Canvas
root = Tk()
# Title of the window			
# root.title("DOOOOOOOOOZ")
root.title("دوووووووووز")
root.resizable(0,0)

#Button
b = [
	[0,0,0],
	[0,0,0],
	[0,0,0]]

#text for buttons
states = [
	[0,0,0],
	[0,0,0],
	[0,0,0]]

for i in range(3):
	for j in range(3):
										
		b[i][j] = Button(
						height = 4, width = 8,
						font = ("Helvetica","20"),
						command = lambda r = i, c = j : clicked(r,c))
		b[i][j].grid(row = i, column = j)


mainloop()		