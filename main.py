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
print(dice)


def rerole_individual(die_number):
    dice[die_number] = random.randint(1,6)


def rerole_all():
    dice[0] = random.randint(1,6)
    dice[1] = random.randint(1,6)
    dice[2] = random.randint(1,6)
    dice[3] = random.randint(1,6)
    dice[4] = random.randint(1,6)
    dice[5] = random.randint(1,6)


turns = list(range(1,14))
for i in turns:
    pass

rerole_all()
print(dice)