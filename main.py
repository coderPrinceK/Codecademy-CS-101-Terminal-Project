import random
from Player import Player
#Test User
User = Player("Conrad", "None",2,3,4,5,6,7,8,9,10,11,12,13,[])


#dice set up
die_one = random.randint(1,6)
die_two = random.randint(1,6)
die_three = random.randint(1,6)
die_four = random.randint(1,6)
die_five = random.randint(1,6)
dice = [die_one, die_two, die_three, die_four, die_five]


def rerole_individual(die_number):
    dice[die_number] = random.randint(1,6)


def rerole_all():
    dice[0] = random.randint(1,6)
    dice[1] = random.randint(1,6)
    dice[2] = random.randint(1,6)
    dice[3] = random.randint(1,6)
    dice[4] = random.randint(1,6)

def re_role_ask():
    die_num = -1
    die_num_string = 0
    for die in dice:
        die_num += 1
        die_num_string +=1
        answer = input("Would you like to rerole die {DIE}? Type Yes or No".format(DIE=die_num_string))
        while answer not in Y_N_choices:
            answer = input("That was not Yes or No please type one exactly!")
        if answer == "Yes":
            rerole_individual(die_num)
            print("Ok the die will be reroled")
        elif answer == "No":
            print("This die will not be changed")

#turns = list(range(1,14)) for when the game is ready the other turns is for testing
turns = []
Y_N_choices = ["Yes", "No"]
#User.print_score_sheet()

print("Welcome to solo Yahtzee.")
for i in turns:
    print("Here are the dice on your first role")
    rerole_all()
    print(dice)
    first_choice = input("Would you like a chance to roll again? Yes or No")
    while first_choice not in Y_N_choices:
        first_choice = input("please type Yes or No.")
    
    if first_choice == "Yes":
        print("Yes Works")
    
    
    else:
        print("No Works")    

print(dice)
re_role_ask()
print(dice)