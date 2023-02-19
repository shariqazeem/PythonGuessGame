import random
true_number = random.randint(1, 100)

guess_number = int(input('Enter your guess between 1 and 100: '))

while True:
    if guess_number == true_number:
        print('YOU ARE RIGHT! GOOD JOB')
        break

    elif guess_number < true_number:
        print('YOUR GUESS IS LOW, PLEASE TRY AGAIN')
        guess_number = int(input('Enter your guess between 1 and 100: '))

    elif guess_number > true_number:
        print('YOUR GUESS IS HIGH, PLEASE TRY AGAIN')
        guess_number = int(input('Enter your guess between 1 and 100: '))
