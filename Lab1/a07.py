import random
from time import time

random.seed(time())

suits = ['s', 'h', 'd', 'c']
cards = [str(i) for i in range(2, 10)] + ['T', 'J', 'Q', 'K', 'A']

class Deck():
	cards=[]
	def create(self):
		self.cards=[]
		for suit in suits:
			for card in cards:
				self.cards.append(suit+card)


	def shuffle(self):
		random.shuffle(self.cards)

	def deal(self, hands, card_num):
		out_hands = []
		for _ in range(hands):
			current_hand = []
			for _ in range(card_num):
				current_hand.append(self.cards.pop())
			out_hands.append(current_hand)
		return out_hands


new_deck = Deck()
new_deck.create()
new_deck.shuffle()
print(f"Dealt hands: {new_deck.deal(3, 5)}")
