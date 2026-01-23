def is_prime(n):
    for i in range(2, n//2):
        if n % i == 0:
            return False

    return True

try:
	amount = int(input("Test number for prime: "))

	if amount < 0:
	    raise Exception
	else:
	    print(f"Number is {'' if is_prime(amount) else 'not '}prime!")

except Exception as e:
	print("Bad number!")
