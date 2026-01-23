import random
from time import time

consecutive_tails = 0
consecutive_heads = 0
total_flips = 0

random.seed(time())
choices = ["H", "T"]


while True:
	next = random.choice(choices)
	total_flips += 1
	print(f"{next}", end=' ')

	if next == "H":
		consecutive_heads += 1
		consecutive_tails = 0
	elif next == "T":
		consecutive_tails += 1
		consecutive_heads = 0
	else:
		# wtf
		break

	if consecutive_heads == 3 or consecutive_tails == 3:
		print(f"\nWe got 3 of the same consecutive flips! It only took {total_flips} flips to get there!")
		break
