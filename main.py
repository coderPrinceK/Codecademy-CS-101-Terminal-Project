import random
from Player import Player
#Test User
User = Player("Conrad", "None",2,3,4,5,6,7,8,9,10,11,0,13,[])


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
    print(dice)



def re_role_ask():
    re_role_answer = input("would you like to rerole all the dice or just some individual dice? Yes or No")
    while re_role_answer not in Y_N_choices:
        re_role_answer = input("Please enter Yes or No!")
    if re_role_answer == "Yes":
        rerole_all()
    else:

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
    print(dice)

    



def scoring():
    print(avalible_options)
    scoring_answer = input("From the options above what would you like to score?")
    while scoring_answer not in avalible_options:
        print(avalible_options)
        scoring_answer = input("That option does not exist or it has already been scored please choose from the options above.")
   #ones
    if scoring_answer == "Ones":
        User.number_scoreing(dice, 1)
        print("You have chosen Ones!")
        print("Your Ones score will be: {SCORE}".format(SCORE=User.ones_score))
        avalible_options.remove("Ones")
    #twos
    elif scoring_answer == "Twos":
        User.number_scoreing(dice, 2)
        print("You have chose Twos!")
        print("Your Twos score will be {SCORE}".format(SCORE=User.twos_score))
        avalible_options.remove("Twos")
    #threes
    elif scoring_answer == "Threes":
        User.number_scoreing(dice, 3)
        print("You have chosen Threes!")
        print("Your Threes score will be {SCORE}".format(SCORE=User.threes_score))
        avalible_options.remove("Threes")
    #fours
    elif scoring_answer == "Fours":
        User.number_scoreing(dice, 4)
        print("You have chosen Fours!")
        print("Your Fours score will be {SCORE}".format(SCORE=User.fours_score))
        avalible_options.remove("Fours")
    #fives
    elif scoring_answer == "Fives":
        User.number_scoreing(dice, 5)
        print("You have chosen Fives!")
        print("Your Fives score will be {SCORE}".format(SCORE=User.fives_score))
        avalible_options.remove("Fives")
    #sixes
    elif scoring_answer == "Sixes":
        User.number_scoreing(dice, 6)
        print("You have chosen Sixes!")
        print("Your Sixes score will be {SCORE}".format(SCORE=User.sixs_score))
        avalible_options.remove("Sixes")
    #3 of a kind
    elif scoring_answer == "3 of a kind":
        print("You have chosen 3 of a kind!")
        three_kind_num = int(input("What number will be used for scoring? Type any number even if you will not recive full points."))
        while three_kind_num not in num_choices:
            three_kind_num = int(input("You must enter a number 1-6!"))
        User.three_kind_scoring(dice,three_kind_num)
        print("Your 3 of a kind score will be {SCORE}".format(SCORE=User.three_kind_score))
        avalible_options.remove("3 of a kind")
    #4 of a kind 
    elif scoring_answer == "4 of a kind":
        print("You have chosen 4 of a kind!")
        four_kind_num = int(input("What number will be used for scoring? Type any number even if you will not recive full points."))
        while four_kind_num not in num_choices:
            four_kind_num = int(input("You must enter a number 1-6!"))
        User.four_kind_scoring(dice,four_kind_num)
        print("Your 4 of a kind score will be {SCORE}".format(SCORE=User.four_kind_score))
        avalible_options.remove("4 of a kind")
    # Full House
    elif scoring_answer == "Full House":
        print("You have chosen Full House!")
        FH_three_num = int(input("What is the number you will select for your set of three?"))
        while FH_three_num not in num_choices:
            FH_three_num = int(input("Please select a number 1-6!"))
        FH_two_num = int(input("Now what will be the number for you pair?"))
        while FH_two_num not in num_choices:
            FH_two_num = int(input("Please select a number from 1-6!"))
        User.full_house_scoring(dice,FH_three_num, FH_two_num)
        print("You Full House Score will be {SCORE}".format(SCORE=User.full_house_score))
        avalible_options.remove("Full House")
    # Sm. Straight
    elif scoring_answer == "Sm. Straight":
        print("You have chosen Sm. Straight!")
        User.SM_straight_scoring(dice)
        print("You Sm. Straight score will be {SCORE}".format(SCORE=User.sm_straight_score))
        avalible_options.remove("Sm. Straight")
    # Lg. Straight
    elif scoring_answer ==  "Lg. Straight":
        print("You have chosen Lg. Straight!")
        User.LG_straight_scoring(dice)
        print("You Lg. Straight score will be {SCORE}".format(SCORE=User.lg_straight_score))
        avalible_options.remove("Lg. Straight")
    #Yahtzee
    elif scoring_answer == "Yahtzee":
        print("You have chosen Yahtzee!")
        User.yahtzee_scoring(dice)
        print("Your Yahtzee score will be {SCORE}".format(SCORE=User.yahtzee_score))
        avalible_options.remove("Yahtzee")
    #Chance
    elif scoring_answer ==  "Chance":
        print("You have chosen Chance!")
        User. chance_scoring(dice)
        print("Your Chance score will be {SCORE}".format(SCORE=User.chance_score))




avalible_options = ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes", "3 of a kind", "4 of a kind", "Full House", "Sm. Straight", "Lg. Straight", "Yahtzee", "Chance"]
#turns = list(range(1,14)) for when the game is ready the other turns is for testing
turns = [1,1]
Y_N_choices = ["Yes", "No"]
#User.print_score_sheet()
num_choices = [1,2,3,4,5,6]

print("Welcome to solo Yahtzee.")
for i in turns:
    print(" ")
    print("Here are the dice on your first role")
    rerole_all()
    first_choice = input("Would you like a chance to roll again? Yes or No")
    while first_choice not in Y_N_choices:
        first_choice = input("please type Yes or No.")
    
    if first_choice == "Yes":
        re_role_ask()
    
    else:
        scoring()    


