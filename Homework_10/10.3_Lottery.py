
import random

numberlist = []


def generate_numbers():
    print "Welcome to the Lottery numbers generator."
    amount_numbers = raw_input("Please enter how many random numbers would you like to have: ")
    amount_numbers = int(amount_numbers) - 1


    while len(numberlist) <= amount_numbers:
        numberlist.append(random.randint(1, 50))

    print numberlist
    print "END"

print generate_numbers()
