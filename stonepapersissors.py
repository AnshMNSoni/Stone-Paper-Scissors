# Day :: 4 -> Stone, Paper and Sissor Game

stone = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

from random import *

sum = 0

for i in range(0, 5):
    computer = randint(0, 2)

    user = int(input("What's your choice? Type 0 for stone, 1 for Paper or 2 for Scissors.\n"))

    if (user == 0):
        print(stone)
    elif (user == 1):
        print(paper)
    elif(user == 2):
        print(scissors)
    else:
        print('Please Read Carefully and Run Again.')   
        break 
        
    print('Computer Choice:\n')
    
    
    if (user == 0):
        if (computer == 0):
            print(stone)
            print("Match Draw\n")
        elif (computer == 1):
            print(paper)
            print("You Lose\n\n")
        else:
            print(scissors)
            print("You Win\n")
            sum += 1
            
    elif (user == 1):
        if (computer == 0):
            print(stone) 
            print("You Win\n")
            sum += 1
        elif (computer == 1):
            print(paper)
            print("Match Draw\n")
        else:
            print(scissors)
            print("You Lose\n")
    
    elif (user == 2):
        if (computer == 0):
            print(stone)
            print("You Lose\n")
        elif (computer == 1):
            print(paper)
            print("You Win\n")
            sum += 1
        else:
            print(scissors)
            print("Match Draw\n")

print(f"Your Score is {sum}")
    