#===============================================================================
# Program Name: CheckRange
# Name: Keegan Bramlet
# Date: 11/28/22
# Purpose of a Program: Print how many times a random number chosen from range (1, 15) is
#                                       between the range (1, 10) if it is chosen 20 times.
#===============================================================================
import random

numbers= [random.randrange(1, 15) for i in range(20)]
# delete the # below to check the randomly created list
# print(numbers)

numbers_new= [x for x in numbers if x <= 10 and x >= 1]


print("The amount of times the random number was in the given range:", len(numbers_new))


