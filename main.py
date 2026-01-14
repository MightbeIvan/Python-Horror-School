import time
import os
import random
import sys

phone_used = False
book_read = False
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
    time.sleep(2)

    os.system("cls" if os.name == "nt" else "clear")
    type("The lights flicker.")
    print()
    time.sleep(0.5)
    
    type("For a moment, All the lights completely shut off.")
    print()
    time.sleep(0.5)

    input("(Press Enter)")
    print()
    
    time.sleep(0.5)
    type("The lights return. Something feels closer.")
    print()
    time.sleep(0.5)

def HomeroomChoice():
    global phone_used, book_read
    
    while True:
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
            die("The voice waits \n You were never meant to hear it.")
            
        else:
            type("Your vision goes blurry")
            print()
            
            type("You feel funny and you start hallucinating")
            print()
            
            type("you see a clock which says 3:15")
            print()
            
            die("You feel the darkness getting closer,you should not have stayed.")

def bathroom_scene():
    clear()
    type("You push the bathroom door open..")
    
    print()
    input("(Press Enter)")
    
    type("The smell hits you immidietly")
    type("Old water. Rust. Something sweet underneath.")
    
    print()
    type("The lights flicker but stay on ")
    type("All the stalls remain closed.")
    
    print()
    type("The mirror strectches tall over the stalls.")
    type("Your reflection looks slightly delayed.")
    
    while True:
        type("What do you do?")
        type("1. Look in the Mirror")
        type("2. Check the stalls")
        type("3. Read the Graffiti")
        type("4. Leave the bathroom")
        
        Br_Choice = input("> ").strip().replace(" ","")
        
        #Mirror 
        if Br_Choice == "1":
            clear()
            type("You step closer to the mirror.")
            type("Your reflection stares back at you")
            
            print ()
            input("(Press Enter)")
            type("It doesn't blink when you do")
            type("Its mouth moves a second too late.")
            
            print()
            type("Your reflection whispers: ")
            type("You stayed past 3:15.")
            
            print()
            input("(Press Enter)")
            type("You stumble backwards, Your heart racing.")
            
        #Stalls (This kills you.)
        elif Br_Choice == "2":
            clear()
            type("You aprach the stalls")
            type("The first stall is locked")
            type("The Second stall is also locked")
            
            print()
            input("(Press Enter)")
            
            type("The third stall cracks open by itself and creaks loudly.")
            print()
            
            input("(Press Enter)")
            type("Something wet drips unto the floor from the celing")
            print()
            
            die("A hand shoots out of the darkness \n You never hit the floor.")
            
        #Graffiti (Lore drop)
        elif Br_Choice == "3":
            clear()
            type("You read the graffiti on the wall")
            
            print()
            type("Names are carved everywhere.")
            type("Some Crossed out. Others circled")
            
            print()
            type("One message repeats over and over:\n")
            type("DO NOT ANSWER AFTER 3:15")
            
            print()
            type("Below it,Written smaller:/n")
            type('"Elliot Tried to warn us", "We did not lisen"')
            
            print()
            type('Another line is written underneath, Fresher,more violent:')
            type('"The School lisens in here')
            
            print()
            type("You feel watched.")
            
            print()
            input("(Press Enter To Continue)")
            
        elif Br_Choice == "4":
            clear()
            type("You turn for the door")
            
            print()
            input("(Press Enter)")
            
            type("The lights shut behind you.")
            
            time.sleep(2)
            input("(Press Enter)")
            
            type("You are back in the hallway")
            return
            
        else:
            type("Your voice echos wrong in thhe room.")
            
    
    
    

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
    time.sleep(0.5)
    input("(Press Enter)")
    os.system("cls" if os.name == "nt" else "clear")

    type('You find yourself standing in a dim room,looks like a classroom but its empty',0.03)
    print()
    time.sleep(0.5)

    type('only thing in view is a table with a book on it that says “Escape Plan…',0.03)
    print()
    time.sleep(0.5)
    input("(Press Enter)")

    type('There is also a sketchy looking landline phone,extremely dusty and looks like its covered with spider webs',0.03)
    print()
    time.sleep(0.5)

    type('Perchance you can call your parents?', 0.03)
    print()
    time.sleep(0.5)
    input("(Press enter to continue)")

    LightEffect()
    print()
    
    input("(Press Enter To Continue)")
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
    type("You are not alone…\n",0.3)
    print()
    
    input("(Press Enter to continue)")

def hallway_scene():
    clear()
    
    type("You step into the hallway")
    print()
    input("Press Enter to Contnue")
    print()
    type("Lockers line in the walls, some dented,  Some hanging open.",0.05)
    
    type("The lights buzz unevenly.",0.05)
    type("on the right side of the hallway,there is a door that says Auditorium",0.05)
    print()
    type('At the far end,there is a room with the words "Library" written in bold fancy letters',0.05)
    input("Press Enter To Coninue")
    
    while True:
        print()
        type("what do you do?")
        type("1. Check the lockers")
        type("2. Go to the Library")
        type("3. Go to the Auditorium")
        
        choice2 = input(">")
        
        if choice2 == "1":
            type("A locker suddenly slams shut beside you.")
            type("You walk towards the general area of the lockers.")
            print()
            type("Something mysterious jumps out the lockers,its a hand,it grabs your leg and pulls you inside of the locker")
            die("The darkness slowly consumes you.")
            
        elif choice2 == "2":
            Library_scene()
            return
        
        elif choice2 == "3":
            bathroom_scene()

def hallway2_From_Library():
    input("(Enter to continue)")

    clear()
    type("You wake up on diferent color tiles,its cold and quiet, you're not in the library anymore.")
    print()

    type("You're in a hallway but its not the same as the last one,this hallway is longer and darker.")
    print()

    type("At the end of this halway,The library is stil there,This time,there's a big sign on the door")
    type('The sign says "Closed" and under it,written in a thick red substance,it says "You know too many things about this school"')
    
    print()
    input("(Press Enter)")
    
    type("The school knows that you noticed.")
    input("(Press Enter )")
    clear()
    type("End Of day one")
    
    # print()
    # type('Close to the library,there is a room next to it with "Main Office" writen on it')
    # type("There is also a creepy looking bathroom next to it")

    print()
    




def Library_KO():
    clear()
    type("Your vision blurs.")
    
    print()
    type("Your head feels heavy")
    
    print()
    input("(Press Enter)")
    
    clear()
    type("You wake up somewhere else.")
    hallway2_From_Library()


def Library_scene():
    clear()
    
    type("You step into the Library")
    print()
    
    input("(Press Enter)")
    print()
    
    type("The air is stale. Dust coats every surface.")
    print()
    
    type("None of the lights reach the far corners.")
    print()
    input("(Press Enter to cntinue)")
    type("The bookshelves are freakishly long and tall.")
    print()
    
    type("Along the right side of the library, a single book lies open,with the pages already tuned.")
    print()
    
    type("what do you choose to examine?")
    print()
    
    type("1.The open book")
    type("2.The Yearbooks")
    type("3. Leave the library")
    
    while True:
        libchoice = input("> ")
        print()
    
        if libchoice == "1":
            
            type("You read the open book")
            print()
            
            type("The text looks hand-written, not printed.")
            print()
            
            type("it reads:")
            print()
            
            type("If you found this, you are still early.")
            print()
            
            type("Most of us weren't.")
            print()
            
            input("Press Enter to Turn The Page")
            print()
            
            type("You turn the page.")
            print()
            
            type("It reads: ")
            print()
            
            type("The phones were installed after the first dissaperance")
            print()
            
            type("The were meant to keep the students and teachers calm")
            print()
            
            type("But they learned to lie instead.")
            print()
            
            type('in shakier ink it said: "The Phones Know How To Lie"')
            print()
            
            input("Press Enter")
            clear()
            
            Library_KO()
            return
        


        #After you look up from the book,you should feel drowsy and slwwpy,close your eyes and opwn them back up to see yourself back in the hallways,this time 
        #The library has a big sign that says "closed, you know too many things about the library"
    

        elif libchoice == "2":
            type("You pull a yearbook of a shelf,the yearbook of this current year,1974.")
            type("The Faces stare back at you,blinking and breathing")
            type("Some faces have been violently scratched out with what looks like red ink.")
            
            type("One name apeared again and again,circled in bold red ink")
            type("The name is ELLIOT MARROW")
            print()

            input("(Press enter to continue)")

            type("A note is scribbled next to his name")
            type('it reads : "He noticed before the rest of us."')

            print()
            input("Press Enter")
            #Same knckout techique...
            Library_KO()

        elif libchoice == "3":
            type("As you step away from the shelves")
            type("A book falls somewhere behind you")
            type("You do not turn around")
            type ("As you walk out the door,you notice something strange,the hallways have shifted")
            #Same KO tech
            Library_KO()
        
        else:
            die("The Darkness slowly but surely swallows you.")




intro()
Enter_Homeroom()
HomeroomChoice()
hallway_scene()
