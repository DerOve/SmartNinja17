#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Program greets user and describes what's the purpose of the program
print "Hello, I will convert kilometers into miles for you"

while True:
    print "Please enter a number of kilometers" #Program asks user to enter number of kilometers.
    km = raw_input("Kilometers: ") #User enters the amount of kilometers.

    try:
        km = float(km.replace(",", "."))
        miles = km * 1.60934 #Program converts these kilometers into miles and prints them.

        if km == 1:
            print str(km) +" kilometer is " + str(miles) + " miles."
        else:
            print str(km) +" kilometers are " + str(miles) + " miles."


    except ValueError:
        print "You have to use numbers"

    choice = raw_input("Would you like to do another conversion (y/n): ") #Program asks user if they'd want to do another conversion.

    if choice.lower() != "y" and choice.lower() != "yes": #If yes, repeat the above process (except the greeting).
        print "Goodbye" #If not, program says goodbye and stops.
        break