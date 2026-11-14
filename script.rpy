define y = Character("You")
define s = Character("Stepdad")
define k = Character("Kidnapper")
define n = Character("Nikki")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file "bg café.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg cafe

    show nikki at left, Transform(zoom=2.0)
    show you at right, Transform(zoom=2.5)

    n "byeeee"
    y "see you later :)"
    
    scene bg dark alley

    show you at center, Transform(zoom=2.5)

    "Walking along your normal route, you suddenly sense a cold presence behind you..."
    "You turn around..."

    scene bg black
    "And everything goes black."
    
    scene bg horror room
    show you at center, Transform(zoom=2.5)

    "You wake up, only to find yourself in a room straight out of a thriller, bound by handcuffs."
    k "Welcome to my game show!"
    "The crackly sound seems to come from all directions, with no apparent source."
    y "It takes me back 7 years, back when I was still a little girl with no hope."
    menu:
         "Relive memories":
            jump flashback
         "Stay strong and push them out":
            jump strong

label flashback:
    scene bg old room
    "You remember when you were locked in similar rooms by your step-dad, when he left you to figure out how to escape to build 'character'."
    "Every time they got harder and harder, and you spent more and more time in them."
    "The memories always come back to haunt you."
    "But this time your life is on the line."
    "So you push through."
    jump continue
    

label strong:
    "But today is not the time for memories."
    "I need to fight for my life"
    jump continue

label continue:
    scene bg horror room
    show you at center, Transform(zoom=2.5)
    k "You must solve three riddles in order to escape"
    k "If you fail..."

    k "The first riddle: I am an odd number. Take away one letter, and I become even. What number am I?"
    menu:
         "1":
            jump wrong
         "3":
            jump wrong
         "5":
            jump wrong 
         "7":
            jump right   
         "9":
            jump wrong

label wrong:
    k "You have failed. GAME OVER"
    return
label right:
    k "Correct."
            
    k "The second riddle: How many months of the year have 28 days?"
    menu:
         "1":
            jump wrong2
         "4":
            jump wrong2
         "11":
            jump wrong2 
         "12":
            jump right2   
         "7":
            jump wrong2

label wrong2:
    k "You have failed. GAME OVER"
    return

label right2:
    k "Correct."
    k "The final riddle: What single number is the same upside down?"
    menu:
         "1":
            jump wrong3
         "3":
            jump wrong3
         "88":
            jump wrong3 
         "8":
            jump right3  
         "7":
            jump wrong3

label wrong3:
    k "You have failed. GAME OVER"
    return
label right3:
    k "Correct."
    k "These numbers give you the code to the door and to unlock your cuffs. Decide which order they are in?"
    menu:
        "7128":
            jump right4
        "1287":
            jump wrong4
        "8127":
            jump wrong4
        "7812":
            jump wrong4

label wrong4:
    k "The combination you chose is wrong. GAME OVER"
    return

label right4:
    k "The combination you chose is correct. Well done."
    "The door slowly opens with a hiss, while your handcuffs slip off your hands with a bang that echoes throughout the corridor ahead."
    k "Now you have 5 minutes to escape and find the exit. Hope you make it..."
    k "or not."
    scene bg black
    "TO BE CONTINUED"


    # This ends the game.

    return
