import random

# r = random.randrange(-1,11)
r = random.randint(-1,11) # randint will also generate highest value in this case that is 11

print('Do you want to play a guessing game with me?')
print("Type Yes to Start")
print("Type NO to Quit")



answer = str(input('Enter your answer ')).lower()

if answer == "yes":
    print(" Then let's play")

print('Guess a number in between 0 to 10')
top_of_range = input("Type Your number: ")

if top_of_range.isdigit(): # this function is for changing entered digit to int
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time")
        quit()
else:
    print('please type a number next time.')

random_number = random.randint(0,top_of_range) # you have to put lower range and higher range as well

guesse = 0


while True:
    guesse += 1
    user_guess = input('Make a guess  ')
    if user_guess.isdigit(): # this function is for changing entered digit to int
        user_guess = int(user_guess)

    else:
        print('please type a number next time.')
        continue
    if user_guess == random_number:
        print("You got right")
        break
    
    elif user_guess > random_number:
            print('you were above the number')
            print('you got it wrong')
    else:
            print('you got it wrong')
            print('you were below the number!')




print('You got it in', guesse ,'guesses')    








