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


# Card loader and settings
white_card_count = 188
black_card_count = 103
white_card_column = 1
black_card_column = 2
option_column = 3
start_row = 2
white_cards = []
black_cards = []

card_lib = openpyxl.load_workbook("data.xlsx")
card_sheet = card_lib.active

for i in range(0, white_card_count):
    white_cards.append(Card("White", i, 0, card_sheet.cell(row=(i+start_row), column=white_card_column).value))

for i in range(0, black_card_count):
    black_cards.append(Card("Black", i, card_sheet.cell(row=i+start_row, column=option_column).value,
                            card_sheet.cell(row=i+start_row, column=black_card_column).value))
# Game variables
player_num = 5
hand_size = 10
players = []

# TODO make gamevars input()
# TODO write function to populate classes for each card
# TODO write Card class
# TODO write main game loop
# TODO write AI players

# Player setup
for i in range (1, player_num):
    players[i] = Player(True, 0, False, input("What is your name?"))

# Main game loop
