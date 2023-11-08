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
