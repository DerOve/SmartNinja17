#!/usr/bin/env python
# -*- coding: utf-8 -*-



secret = "13"   #Secret number

guess = raw_input("Guess the secret number between 1 - 20!")

while guess != secret:
    print "Try again! Secret number is not " + guess
    guess = raw_input("Guess the secret number between 1 - 20!")
    print guess


    if guess == secret:
        print "Congratulations, " + guess + " is the secret number!"
        break

