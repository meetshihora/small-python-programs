import random

cards = ['Dimond', 'Hearts', 'Spades', 'Clubs']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

def pickRandomCard():
    card = random.choice(cards)
    rank = random.choice(ranks)
    return rank, card

print(pickRandomCard())