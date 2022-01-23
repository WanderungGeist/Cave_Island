dead_poop = '''
         )
        (
          ,
       (___)
      (_____)
     (_______)
  '''

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


print("\nYou have followed your map to the entrance of a cave. This is where your map stops. You must follow clues and make the correct decisions, or die a tragic death.")

input("To enter the cave, press 'Enter' ")

print("\nWelcome to THE CAVE!\n\nAs you move forward, you come to a fork in the path. \nTo the left, you see what looks like old, faded footprints going in, and a sign reading 'Beware!'. \nTo the right you see only darkness.")

fork = input("Which way would you like to go? \nL or R? ").lower()

if fork == ("l"):
  print("\nThe footprints going in don't come back out, and for good reason. \nYou fall in to a pit of spikes and die.")
elif fork == ("r"):
  print("\nYou continue forward into the darkness, feeling along the wall as you go. You feel uneasy. \nThe walls are damp, and smell like mold. You'll definitely want to wash up before you eat again.")
  input("Press 'Enter'")

  

  print("\nMoving forward, you see a dim light in the distance. As you get closer, you realize that the light \nis on an island in the middle of a small lake that takes up the entire floor surface of a MASSIVE cavern, and a sign that reads 'NO SWIMMING'. ")
  input("Press 'Enter'")

  print("\nAs you look across the water, you see a boat sitting at a dock in front of a house. You look around your side again and see a rope tied to a post. \nYou are a strong swimmer and consider swimming across. How would you like to continue? \nA) Swim across \nB) Investigate further")
  lake = input("A or B? ").lower()

  if lake == ("a"):
    print('''
                                        _J""-.
                    .-""L_            /o )   \ ,';
              ;`, /   ( o\           \ ,'    ;  /
              \  ;    `, /            "-.__.'"\_;
              ;_/"`.__.-"
    ''')
    print("Despite being a strong swimmer, giant piranhas are a bit much to handle and you die a painful, bloody death.")

  elif lake == ("b"):
    print("\nA very wise choice. On closer inspection, you notice giant piranhas making a splash in the distance. Swimming could have ended very badly.")
    input("Press 'Enter' to inspect the rope.")  

    print("\nYou pick up the rope and notice that it leads into the water. As you pull on it, the distant boat starts moving toward you. \nThe other end of the rope is attached to the boat!")
    input("Press 'Enter' to pull the boat in and row it to the dock.")

    print("\nYou row the boat to the other side and step onto the rocky shore. \nThere is a small house in front of you that has 3 doors on the front. One red, one yellow, and one blue. No windows are anywhere to be seen. \nThe only thing you notice is a sign posted above the doors.")
    input("Press 'Enter' to read the sign. ")
    print("\nThe sign reads: \nChoices made and choices lost. \nOne you win, and two have cost. \nOne burns red and causes strife, \nOne, with teeth, makes blue your life. \nOnly gold is treasure told.\nChoose the path your future holds.")

    input("\nPress 'enter' to chooose a door.")
      
    door = input("R, Y, or B: ").lower()
      
    if door == ("r"):
      print('''
       _.-._
      ({  ` )
       ` |''
        \_/
 .(      |      ),
`  -----' `-----  '
        ''')
      print("You open the red door, and a giant ball of fire rushes toward you, rendering you into a pile of ash. \nSO CLOSE!")
    elif door == ("b"):
      print('''
       \ /\_           ___/\__
       /~~~-|_      __|_,-~~-,|__
      |@    \ |  __|_-~        ~-|__
      /  /\  \|/\_-~         ,--   \|
     / /|| \  ~--   / /     /       \
     |//|/  \_  ___/ /      |   __/  \
   ___//      ~//_,,,-----'~~~~~     /
  /  o \             ~~~~~~~~~~~~~~~~
  ~//-/~
/~~/\ ~/
~~~~~~~
        ''')
      print("You open the blue door. A giant Dragon rushes toward you, tearing your throat out before you can even blink. Blue?! TEETH?! Come on! Now you're dead.")
    elif door == ("y"):
      print('''
      __________________
    .-'  \ _.-''-._ /  '-.
  .-/\   .'.      .'.   /\-.
 _'/  \.'   '.  .'   './  \'_
:======:======::======:======:  
 '. '.  \     ''     /  .' .'
   '. .  \   :  :   /  . .'
     '.'  \  '  '  /  '.'
       ':  \:    :/  :'
         '. \    / .'
           '.\  /.'    
             '\/'
      ''')
      print("You open the yellow door, thinking to yourself: 'Damn. That riddle was STUPID easy!' \nIn front of you sits a pile of gold and jewels. Congratulations! You're stupid rich! ")
    else:
      print(dead_poop)
      print("You stand still for too long and die of dysentery.")
  else:
    print(dead_poop)
    print("You twist your ankle in the burrow of flesh eating sandworms.")
    input("Press Enter for more options:")
    print("You'll probably want either a closed casket, or cremation in this situation. There's not much left to bury.")
else:
  print(dead_poop)
  print("Standing still attracts flesh eating sandworms. You should probably... Dammit! Not another one... \nI should've said something sooner. \nI really need this job...")
