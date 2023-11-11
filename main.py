import random
from Player import Player
#Test User
User = Player("Conrad", 1,2,3,4,5,6,7,8,9,10,11,12,13)


#dice set up
die_one = random.randint(1,6)
die_two = random.randint(1,6)
die_three = random.randint(1,6)
die_four = random.randint(1,6)
die_five = random.randint(1,6)
die_six = random.randint(1,6)

dice = [die_one, die_two, die_three, die_four, die_five, die_six]

def print_dice():
    print(dice)

def rerole_individual():
    return random.randint(1,6)

turns = list(range(1,14))
for i in turns:
    print_dice()
