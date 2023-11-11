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
        #replace theses so the match the ones above
        print("Full House: "+self.full_house_score)
        print("Sm. Straight: "+self.sm_straight_score)
        print("Lg. Straight: "+self.lg_straight_score)
        print("Yahtzee: "+self.yahtzee_score)
        print("Chance: "+self.chance_score)
