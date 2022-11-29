#===============================================================================
# Program Name: SumOfFood
# Name: Keegan Bramlet
# Date: 11/28/22
# Purpose of a Program: Sum the price of each food item in a dictionary
#===============================================================================
def SumOfFood(foodDict):
    foodDict = { "Pizza": 3.50, "Sandwich": 5.30, "Hamburger": 9.45, "Spaghetti": 5.75}
    total= round(sum(foodDict.values()), 2)
    print("The sum of the price of food is $",total)

foodDict = { "Pizza": 3.50, "Sandwich": 5.30, "Hamburger": 9.45, "Spaghetti": 5.75}
SumOfFood(foodDict)
