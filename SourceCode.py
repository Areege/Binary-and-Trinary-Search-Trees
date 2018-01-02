import random
import time

#-----------------------------------------------------------------------------------
# This binary search function takes a list and a target value. It then searches the
# list for that target value. If the target value is found, the function returns the
# index value at where it is located in the list. And, if the target value is not found,
# the function returns -1.
#-----------------------------------------------------------------------------------
def binarySearch(collection, target):
    low = 0
    high = len(collection) -1
    while high >= low:
        mid = (high + low) //2
        if (target == collection[mid]):
            return mid
        #search left half of collection
        if (target < collection[mid]):
            high = mid - 1 
        #search right half of collection
        else:
            low = mid + 1    
    return -1 

#-----------------------------------------------------------------------------------
# This trinary search function takes a list and a target value. It then searches the
# list for that target value. If the target value is found, the function returns the
# index value at where it is located in the list. And, if the target value is not found,
# the function returns -1.
#-----------------------------------------------------------------------------------
def trinarySearch(collection, target):
    low = 0
    high = len(collection) -1
    while high >= low:
        one_third = low + (high-low)//3
        two_thirds = low + 2*(high-low)//3
        if (target == collection[one_third]):
            return one_third
        #search the left-hand third
        elif (target < collection[one_third]):
            high = one_third - 1
        elif (target == collection[two_thirds]):
            return two_thirds
        #search the middle third
        elif (target < collection[two_thirds]):
            low = one_third + 1
            high = two_thirds - 1
        #search the right-hand third
        else:
            low = two_thirds + 1
    return -1

#-----------------------------------------------------------------------------------
# This sorting function takes a list as a parameter and sorts the list in the order
# of least to greatest.
#-----------------------------------------------------------------------------------
def selectionSort(aList):
   for fill in range(len(aList)-1,0,-1):
       maxPosition = 0
       for index in range(1,fill+1):
           if aList[index]>aList[maxPosition]:
               maxPosition = index
       temp = aList[fill]
       aList[fill] = aList[maxPosition]
       aList[maxPosition] = temp


#-----------------------------------------------------------------------------------
# This function takes a value n as a parameter and creates a list of n randomly
# generated even numbers, then returns it.
#-----------------------------------------------------------------------------------
def createList1(n):
    #generate a list of random integers
    aList = random.sample(range(1, 16001), n)
    #make sure that there are only even integers in the list
    for index in range(0, len(aList)-1):
        if (aList[index] % 2 != 0):
            aList[index] = aList[index] + 1
    return aList

#-----------------------------------------------------------------------------------
# This function takes a value n as a parameter and creates a list of n randomly
# generated odd numbers, then returns it.
#-----------------------------------------------------------------------------------
def createOddList(n):
    #generate a list of random integers
    aList = random.sample(range(1, 1000000), 10*n)
    #make sure that there are only odd integers in the list
    for index in range(0, len(aList)-1):
        if (aList[index] % 2 == 0):
            aList[index] = aList[index] + 1
    return aList

#-----------------------------------------------------------------------------------
# This function takes a list as a parameter and creates a new list that contains
# 10 copies of each value in the list provided (in order). It then returns the new
# list.
#-----------------------------------------------------------------------------------
def createList2(list1):
    list2 = []
    for integer in range(0, len(list1)):
        for index in range(0,10):
            list2.append(list1[integer])
            index = index + 1
    return list2

#-----------------------------------------------------------------------------------
# This function takes two lists as parameters and measures/prints out the total time
# it takes to use binary and trinary search functions in the context of this assignment.
#-----------------------------------------------------------------------------------
def checkTime(list1, list2):
    t0 = time.clock()
    for index in list2:
        result1 = binarySearch(list1, index)
    print("Binary Search time: " + str(time.clock()-t0)) 
    t0 = time.clock()
    for index in list2:
        result2 = trinarySearch(list1, index)
    print("Trinary Search time: " + str(time.clock()-t0) + "\n")

#-----------------------------------------------------------------------------------
# This function takes a value n as a parameter and runs through the functions required
# to complete the experiments for this assignment.
#-----------------------------------------------------------------------------------
def testing(n):
    print("Experiment #1")
    list1 = createList1(n)
    selectionSort(list1)
    list2 = createList2(list1)
    checkTime(list1, list2)
    print("Experiment #2")
    list2 = createOddList(n)
    checkTime(list1, list2)

#-----------------------------------------------------------------------------------
# The main function makes sure that all values of n are tested for.
#-----------------------------------------------------------------------------------
def main():
    nValues = [1000, 2000, 4000, 8000, 16000]
    for index in nValues:
        print("For n = " + str(index) + "\n")
        testing(index)

main()





