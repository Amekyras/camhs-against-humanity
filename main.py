import openpyxl
import random
import os


def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')


class Card:
    def __init__(self, card_colour, card_id, card_options, card_text):
        self.colour = card_colour
        self.id = card_id
        self.pc = card_options
        self.text = card_text


class Player:
    def __init__(self, player_id, player_is_human, player_score, player_is_czar, player_name):
        self.id = player_id
        self.human = player_is_human
        self.score = player_score
        self.czar = player_is_czar
        self.name = player_name
        self.hand = []

    def add_score(self):
        self.score += 1

    def reset_score(self):
        self.score = 0

    def add_card(self):
        self.hand.append(white_cards.pop())

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
    white_cards.append(Card("White", str(i)+"W", 0, card_sheet.cell(row=(i+start_row), column=white_card_column).value))

for i in range(0, black_card_count):
    black_cards.append(Card("Black", str(i)+"B", card_sheet.cell(row=i+start_row, column=option_column).value,
                            card_sheet.cell(row=i+start_row, column=black_card_column).value))
# Game variables
player_num = 1
hand_size = 10
players = []

# TODO make gamevars input()
# TODO write function to populate classes for each card
# TODO write Card class
# TODO write main game loop
# TODO write AI players

# Player setup
for i in range(0, player_num):
    players.append(Player(i, True, 0, False, input("What is your name?")))
clearscreen()
# Main game loop
# Give players cards
random.shuffle(white_cards)
for i in range(0, len(players)):
    while len(players[i].hand) < hand_size:
        players[i].add_card()
for i in range(0, 10):
    print(players[0].hand[i].text)
# check if Czar exists
