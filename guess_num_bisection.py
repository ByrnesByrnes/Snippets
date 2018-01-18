print("Please think of a number between 0 and 100!")

user_num	= int(input("input a guess: "))

num_guesses = 0
low 	= 0
high 	= 100
guess = (high + low) / 2

while user_num != guess:
	print(f"is this your number {guess}?")
	""" User guess is either higher or lower. If user guess is L you want it to go up so
	you respond with a high guess and vice versa."""
	user_1 = input("high or low: h or l or is answer correct c? ")
	if user_1 == "h":
		high = guess

	elif user_1 == "l":
			low = guess
				
	elif user_1 == "c":
		break
	else:
		print("input accuracte number")
	guess = (high + low)/2
	num_guesses += 1

print(f"Game over. Your secret number was: {guess}")

