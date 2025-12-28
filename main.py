import time
import os
import random
import sys

phone_used = True
book_read = True
HrChoices = True

def clear():
    os.system("cls" if os.name == "nt" else "clear")
    
def type(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
#Death
def die (message):
    sys.exit(f"{message}\n GAME OVER")

def use_phone():
    type("\nYou lift the receiver.")
    input("(Press Enter)")

    type("Silence...")
    input("(Press Enter)")

    type("A voice whispers:")
    type('"Why did you stay after class?"')
    input("Press enter to continue")

#Light effects (TO build suspense)
def LightEffect():
    
    os.system("cls" if os.name == "nt" else "clear")
    type("The lights flicker.")
    print()
    
    type("For a moment, All the lights completely shut off.")
    print()
    
    input("(Press Enter)")
    print()
    
    type("The lights return. Something feels closer.")
    print()

def HomeroomChoice():
   
    
    while HrChoices:
        print()
        type("What do you do?")
        type("1. Read the book")
        type("2. Use the phone")
        
        choice =input(">").strip()
        
        if choice == "1":
            read_book()
            phone_used = False
            break
            
        elif choice == "2":
            use_phone()
            book_read = False
            break
            
        else:
            type("Your vision goes blurry")
            print()
            
            type("You feel funny and you start hallucinating")
            print()
            
            type("you see a clock which says 3:15")
            print()
            
            die("You feel the darkness getting closer,you should not have stayed.")
            
        
        
        
    
    
    


#Read the book in the Homeroom Room.

def read_book():
    type("You Open the book")
    type("Most of its pages are blank")
    
    print()
    input("(Press Enter To Continue)")
    
    type("One sentence is writen in shaky ink.")
    type('It reads : “Do not answer the phone after 3:15"')
    
    print()
    input('(Press Enter to continue)')
    
    print()
    type("The Landline phone Instantly burst into violent flames.")
    print()
    
    type("A big door creaks and open in front of you,it looks like its leading to a hallway.")
    type("You have no choice but to go through the door.")
    print()

#Use the phone in the Homeroom room (this kills you)

def Enter_Homeroom():
    type('There is only one door in front of you..It is labeled as "Homeroom 1228” ',0.03)
    print()
    
    input("(Press Enter to approach the door)")
    print()
    
    type("The paint is chipped, and the handle is ice cold,Refreshing even..",0.03)
    print()
    
    input("(Press Enter to open the door)")
    print()
    
    type("The door creaks loudly as you step inside...\n",0.03)
    print()
    
    type('You find yourself standing in a dim room,looks like a classroom but its empty',0.03)
    print()
    
    type('only thing in view is a table with a book on it that says “Escape Plan…',0.03)
    print()
    
    type('There is also a sketchy looking landline phone,extremely dusty and looks like its covered with spider webs',0.03)
    print()
    
    type('Perchance you can call your parents?', 0.03)
    print()
    
    LightEffect()
    print()
    
    input("Press Enter To Continue")
    print()
    
    



def intro():
    os.system("cls" if os.name == "nt" else "clear")
    type("You spawn in a dark room..",0.05)
    print()
    
    input("(Press Enter to continue)")
    print()
    
    type("The air smells like dust and old paper.",0.05)
    print()
    
    type("A flickering fluorescent light buzzes overhead.\n",0.05)
    print()
    
    input("(Press Enter to continue)")
    print()
    
    type("Desks are scattered across the floor.",0.05)
    type("A clock on the wall is frozen at 10:36.\n",0.05)
    print()
    
    input("(Press Enter to continue)")
    print()
    
    type("You don’t remember how you got here.",0.05)
    type("Somewhere in the school, a door creaks...loud,very disturbing \n",0.05)
    print()
    
    input("(Press Enter to continue)")
    os.system("cls" if os.name == "nt" else "clear")
    
    print()
    type("You are not alone…\n",0.5)
    print()
    
    input("(Press Enter to continue)")

def hallway_scene():
    clear()
    type("You step into the hallway")
    print()
    input("Press Enter to Contnue")
    
    type("Lockers line in the walls, some dented, some hanging open. Some hanging open.")
    type("The lights buzz unevenly.")
    type("on the right side of the hallway,there is a door that says Bathroom")
    type('At the far end,there is a room with the words "Library" written in bold fancy letters')
    input("Press Enter To Coninue")
    
    while True:
        type("what do you do?")
        type("1. Check the lockers")
        type("2. Go to the Library")
        type("3. Go to the Bathroom")
        
        choice2 = input(">")
        
        if choice2 == "1":
            type("A locker suddenly slams shut beside you.")
            type("You walk towards the general area of the lockers.")
            type("Something mysterious jumps out the lockers,its a hand,it grabs your leg and pulls you inside of the locker")
            die("The darkness slowly consumes you.")

    
    
    


intro()
Enter_Homeroom()
HomeroomChoice()

if book_read == True:
    hallway_scene()