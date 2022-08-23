from random import randint


# The first parameter is the initial value of the range. The second parameter is the final value of the range.
def guess_the_number(start, finish):
    number = randint(start, finish)
    print('Welcome to the game: "Guess the number"!\n' + '*' * 40)

    # The function accepts a string and returns True if the string consists of digits and
    # the string converted to a number is within range.
    def is_valid(test):
        return test.isdigit() and start <= int(test) <= finish

    answer = input(f'Guess the number from {start} to {finish}? >>> ')
    # Run a loop that runs until the user’s number and the number computers do not match.
    while answer != str(number):
        if not is_valid(answer):
            answer = (input(f'Or maybe we\'ll still enter an integer from {start} to {finish}? >>> '))
        else:
            if int(answer) < number:
                answer = input('Your number is less than guessed, try again: >>> ')
            elif int(answer) > number:
                answer = input(f'Your number is bigger than guessed, try again: >>> ')

    print(f'My number is {answer}\nYou guessed, congratulations!\nThank you for playing with me. See you again...')


def main():
    # Calling a function in which integer arguments are a search range.
    guess_the_number(1, 100)


if __name__ == '__main__':
    main()
