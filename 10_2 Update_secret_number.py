#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def main():

    secret = random.randint(1, 20)

    while True:
        guess = int(raw_input("Guess the secret number between 1 - 20!"))

        if guess == secret:
            print " ~~Congratulations, you guessed the secret number! It is %s!~~" % secret
            break
        elif guess < secret:
            print " "
            print "Secret number is greater than %s" % guess
        elif   guess > secret:
            print " "
            print "Secret number is smaller than %s " % guess

        elif guess > 20:
            print " "
            print "Secret number must be between 1 and 20!"

print main()


