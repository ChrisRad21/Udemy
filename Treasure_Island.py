print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
lake_action = input("You've come to a lake. There is an island in the middle of the lake. Type wait to wait for a boat. Type swim to swim across.\n").lower()
if lake_action == 'wait':
  print('A boat takes you across to the island')
  house_action = input('You arrive at a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n')
  if house_action == 'red':
    print('You fall into a room full of fire. You succumb to the flames.')
  if house_action == 'yellow':
    print('You found the treasure. Congratulations!')
  if house_action == 'blue':
    print('You choose a trapdoor that leads to your eventual death by spikes.')
  else:
    print("You chose a door that didn't exist. Game Over. At least you didn't die.")
if lake_action == 'swim':
  print('You were eaten by an enourmous tuna that somehow lives in a lake.')
print('Restart to play again!')