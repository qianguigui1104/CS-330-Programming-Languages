
#Pam Qian
#Lab1-3-GuessingGame

import random
import time

#Initialize variables
number = str(random.randint(1, 10))
count = 1
keep_going = True
old_answers = []

#Get user's name and explain rules
name = input('Enter your name: ')
print('\n*Hello,', name, '! Welcome to this number guessing game.*')
time.sleep(0.5)
print('\n*Guess a number between 0 and 10*')
time.sleep(0.5)
print('\n*You have 7 tries*\n')
time.sleep(0.5)

#Keep track of guesses
while keep_going == True and count < 8:
	new_answer = input('Enter your guess: ')

	if new_answer == number: #correct guess
		print(name, ', your guess is correct. Congratulation!\n')
		time.sleep(0.5)
		keep_going = False

	else: #wrong guess
		old_answers.append(new_answer)
		count+=1

		print('Your guess is wrong.')
		time.sleep(0.5)
		print('\n*****Try Again*****')
		time.sleep(0.5)
		print('Your previous guesses:', old_answers)
		time.sleep(0.5)


#If the user won
if count < 8:
	print('Number of guesses you took: ', count)
	print('*Your guesses were:', old_answers, '*\n')
	print('*Bye*')

#If the user ran out of tries
else:
	print('*\n\nSorry, you have run out of tries*\n')
	print('*Your guesses were:', old_answers, '*\n')
	print('The correct answer is', number, '*\n')
	print('*Bye*')




