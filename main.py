import openpyxl

class Card:
    def __init__(self, card_colour, card_id, card_options, card_text):
        self.colour = card_colour
        self.id = card_id
        self.pc = card_options
        self.text = card_text


class Player:
    def __init__(self, player_is_human, player_score, player_is_czar, player_name):
        self.human = player_is_human
        self.score = player_score
        self.czar = player_is_czar
        self.name = player_name

    def add_score(self):
        self.score += 1

    def reset_score(self):
        self.score = 0


# Game variables
player_num = 5
hand_size = 10

# TODO make gamevars input()
# TODO write Player classes
# TODO write function to populate classes for each card
# TODO write Card class
# TODO write main game loop
# TODO write AI players
