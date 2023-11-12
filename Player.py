class Player():
    def __init__(self, name, ones_score, twos_score, threes_score, fours_score, fives_score, sixs_score, three_kind_score, four_kind_score, full_house_score, sm_straight_score, lg_straight_score, yahtzee_score, chance_score):
        self.name = name
        #number scores
        self.ones_score = ones_score
        self.twos_score = twos_score
        self.threes_score = threes_score
        self.fours_score = fours_score
        self.fives_score = fives_score
        self.sixs_score = sixs_score

        #special scores
        self.three_kind_score = three_kind_score
        self.four_kind_score = four_kind_score
        self.full_house_score = full_house_score
        self.sm_straight_score = sm_straight_score
        self.lg_straight_score = lg_straight_score
        self.yahtzee_score = yahtzee_score
        self.chance_score = chance_score

    
    def print_score_sheet(self):
        print("Player: {NAME}".format(NAME=self.name))
        print("__________")
        print("Ones: {ONES}".format(ONES=self.ones_score))
        print("Twos: {TWOS}".format(TWOS=self.twos_score))
        print("Threes: {THREES}".format(THREES=self.threes_score))
        print("Fours: {FOURS}".format(FOURS=self.fours_score))
        print("Fives: {FIVES}".format(FIVES=self.fives_score))
        print("Sixs: {SIXS}".format(SIXS=self.sixs_score))
        print("__________")
        print("3 of a kind: {TKIND}".format(TKIND=self.three_kind_score))
        print("4 of a kind: {FKIND}".format(FKIND=self.four_kind_score))
        print("Full House: {FH}".format(FH=self.full_house_score))
        print("Sm. Straight: {SM}".format(SM=self.sm_straight_score))
        print("Lg. Straight: {LS}".format(LS=self.lg_straight_score))
        print("Yahtzee: {Y}".format(Y=self.yahtzee_score))
        print("Chance: {CHANCE}".format(CHANCE=self.chance_score))


#a function to use on all lower numbers
    def number_scoreing(self,dice_list, number):
        count = 0
        for die in dice_list:
            if die == number:
                count += number
        if number == 1:
            self.ones_score = count
        elif number == 2:
            self.twos_score = count
        elif number == 3:
            self.threes_score = count
        elif number == 4:
            self.fours_score = count
        elif number == 5:
            self.fives_score = count
        else:
            self.sixs_score = count

    def three_kind_scoring(self, dice_list, number):
        minimum_num = 3
        count = 0
        die_count = 0
        for die in dice_list:
            if die == number:
                count += die
                die_count += 1
            else:
                count += die
        
        if die_count >= minimum_num:
            self.three_kind_score = count
        else:
            self.three_kind_score = 0

    def four_kind_scoring(self, dice_list, number):
        minimum_num = 4
        count = 0
        die_count = 0
        for die in dice_list:
            if die == number:
                count += die
                die_count += 1
            else:
                count +=die
        
        if die_count >= minimum_num:
            self.four_kind_score = count
        else:
            self.four_kind_score = 0

    def full_house_scoring(self, dice_list, three_num, two_num):
        three_count = 0 
        two_count = 0
        for die in dice_list:
            if die == three_num:
                three_count += 1
            elif die == two_num:
                two_count += 1
        
        if three_count+two_count == 5:
            self.full_house_score = 25
        else:
            self.full_house_score = 0


    def SM_straight_scoring(self, dice_list):
        dice_list.sort()
        sorted_list =[]
        for die in dice_list:
            if die not in sorted_list:
                sorted_list.append(die)
        
        #fix  index error
        test =  sorted_list[0]+1 == sorted_list[1] and sorted_list[1]+1 == sorted_list[2] and sorted_list[2]+1 == sorted_list[3]
        print(test)