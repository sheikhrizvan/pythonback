import game

print('Guess the number\nYou have 5 chance')
for i in range(1, 5, 1):
	a = int(input('Enter any Number between 1 t0 10 :'))
	game.guessNumber(a)