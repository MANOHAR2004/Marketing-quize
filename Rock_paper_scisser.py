import random

user_wins = 0
computer_wins = 0
options = ["rock","paper","scissor"] #index[0,1,2]
# options = [0,1,2] # You can put indexes in list so they can represent same value as in the list

while True:
    
    answer = str(input("Do you want to play ")).lower()
    if answer == "yes":
        print("Then lets play")
        
    else:
        print("Thanks for comming here")
        quit()
    break

while True:

    user_input = input("Type rock/paper/scissor or Q to Quit.").lower()
    if user_input =="q":
        break
    if user_input not in options:  # Check if the input is valid
        print("Invalid option, please try again.")
    

    

    random_number = random.randint(0,2)
    # rock : 0, paper:1, scissor:2
    computer_pick = options[random_number]
    print("Computer picked:",computer_pick)

    if user_input == "rock" and computer_pick == "scissor":
        print("you won!")
        user_wins +=1
        

    elif user_input == "paper" and computer_pick == "rock":
        print("you won!")
        
        user_wins +=1
        

    elif user_input == "scissor" and computer_pick == "paper":
        print("you won!")
        user_wins +=1

    elif user_input == computer_pick:
        print("this is a tie")    
    else:
        print("you lost!")
        computer_wins +=1
print("Computer won " + str(computer_wins) + " times.")
print("You won " + str(user_wins) + " times.")
print("Goodbye, friend. I had fun playing with you.")





