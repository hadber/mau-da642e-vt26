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
		m = amount + 1
		while True:
			if is_prime(m):
				print(f"Next highest prime number is: {m}")
				break
			m += 1

except Exception as e:
	print("Bad number!")
