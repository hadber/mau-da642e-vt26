try:
	amount = int(input("Enter your age: "))

	if amount < 0:
	    raise Exception
	if amount <= 2:
		print(f"Your age in dog years is: {amount*10.5}")
	else:
	    print(f"Your age in dog years is: {2*10.5 + (amount-2)*4}")
except Exception as e:
	print("The introduced years is bad!")
