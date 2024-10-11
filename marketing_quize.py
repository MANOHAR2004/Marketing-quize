print("welcome to Marketing Quiz show!")

play = input("Do you want to play this quiz; Type - Yes or No? ")


if play != "yes":
    quit()

print("Okay! Let's play: ")
score = 0
name = str(input("Enter your name:"))
section = str(input("Enter your section:")).upper()
roll_number = int(input("Enter your Roll number:"))


answer = input('what does S in S-T-P stand for? ').lower()
if answer == "segmentation":
    print('correct!')
    score += 1
else:
    print('Incorrect Answer')



answer = input('what does T in S-T-P stand for? ').lower()
if answer == "targeting":
    print('correct!')
    score += 1
else:
    print('Incorrect Answer')


answer = input('what does P in S-T-P stand for? ').lower()
if answer == "positioning":
    print('correct!')
    score += 1
else:
    print('Incorrect Answer')

if answer !="no":
    print("Your report card:")
    print("Name:",name)
    print("Section:",section)
    print("Roll_number:",roll_number)
    print("you get " + str(score) + " quetions correct")
    print("you get " + str((score/3) * 100) + "%")

play = input("Do you want to play again? Type - Yes or No: ").lower()
if play != "yes":
    print("Thanks for playing!")



