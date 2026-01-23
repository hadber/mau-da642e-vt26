base_price = 35
discount = 0.6

try:
	amount = int(input("Enter the number of day-old cinnamon buns you'd like: "))
	
	# reasonable amount
	if amount < 1000:
		discount_price = base_price*discount
		print(f"Base price: {base_price:.2f} \t Discounted price: {discount_price:.2f} \t Total: {amount*discount_price:.2f}")
	else:
		raise Exception
except Exception as e:
	print("Bad amount!")
