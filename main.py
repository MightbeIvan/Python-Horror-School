import time
import os
import random
import sys

def clear():
    os.system("cls" if os.name == "nt" else "clear")
    
def type(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
#Death
def death():
    print("Better luck in your next life.")
    return False

def use_phone():
    print("\nYou lift the receiver.")
    input("(Press Enter)")

    print("Silence...")
    input("(Press Enter)")

    print("A voice whispers:")
    print('"Why did you stay after class?"')

#Light effects (TO build suspense)
def LightEffect():
    print("The lights flicker.")
    print("For a moment, All the lights completely shut off.")
    input("(Press Enter)")
    print("The lights return. Something feels closer.")


#Read the book in the Homeroom Room.

def read_book():
    print("You Open the book")
    print("Most of its pages are blank")
    print("Only one page says words,the middle page…\n")
    print('It reads : “USE THE BACKDOOR IN THE BASEMENT TO ESCAPE"')
    input('(Press Enter to continue)')

#Use the phone in the Homeroom room (this kills you)

def Enter_Homeroom():
    print('There is only one door in front of you..It is labeled as "Homeroom 1228” ')
    input("(Press Enter to approach the door)")
    print("The paint is chipped, and the handle is ice cold,Refreshing even..")
    input("(Press Enter to open the door)")
    print("The door creaks loudly as you step inside...\n")
    print('You find yourself standing in a dim room,looks like a classroom but its empty…only thing in view is a table with a book on it that says “Escape Plan…')
    print('There is also a sketchy looking landline phone,extremely dusty and looks like its covered with spider webs…Perchance you can call your parents?')

def enter():
    input("Press Return/Enter To Continue.\n")

def intro():
    type("You spawn in a dark room...\n",0.1)
    
    clear()
    enter()
    
    type("The air smells like dust and old paper.",0.1)
    type("A flickering fluorescent light buzzes overhead.\n",0.1)
    
    enter()
    
    type("Desks are scattered across the floor.",0.1)
    type("A clock on the wall is frozen at 10:36.\n",0.1)
    
    enter()
    
    type("You don’t remember how you got here.",0.1)
    type("Somewhere in the school, a door creaks...loud,very disturbing \n",0.1)
    
    enter()
    clear()
    
    type("You are not alone…\n",0.5)
# Call this before the game loop

clear()
intro()
Enter_Homeroom()
