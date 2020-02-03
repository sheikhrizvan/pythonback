from random import *
def guessNumber( guess):
	a = randint(1,10)
	if(guess == a):
		print('WooHooooo!!!!!... Your Got It!!..')
	else:
		print('Woooops......, Try One More time...\nNumber is: ', a)