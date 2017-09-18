#!/usr/bin/env python
# -*- coding: utf-8 -*-



number = raw_input("Hallo, enter a number between 1 and 100:")
number = int(number)



for x in range(1, number+1):

    if x % 3 == 0 and x % 5 == 0:
        print "fizzbuzz"

    elif x % 3 == 0:
        print "fizz"

    elif x % 5 == 0:
        print "buzz"

    else:
        print x