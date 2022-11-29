#===============================================================================
# Program Name: Unique
# Name: Keegan Bramlet
# Date: 11/28/22
# Purpose of a Program: Find Unique values of list
#===============================================================================
def unique(list1):
    list_set = set(list1)
    unique_list = (list(list_set))
    for x in unique_list:
        print("the unique values from the list is", x)
     
list1 = [1, 3, 3, 3, 6, 2, 3, 6, 5, 4, 2]
unique(list1)
