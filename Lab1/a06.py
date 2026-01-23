import random
from time import time

random.seed(time())

suits = ['s', 'h', 'd', 'c']
cards = [str(i) for i in range(2, 10)] + ['T', 'J', 'Q', 'K', 'A']

def make_deck():
	deck = []

	for suit in suits:
		for card in cards:
			deck.append(suit+card)

	return deck


deck_of_cards = make_deck()
print("Original deck: ", deck_of_cards)
random.shuffle(deck_of_cards) # shuffle the deck
print("Shuffled deck: ", deck_of_cards)
