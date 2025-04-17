#Binary Search
#Implementation of binary search algorithm in Python
#We will prove that the binary search algorithm is faster than naive search algorithm
#naive Search => scan entire list and ask if its equal to the target
#if yes , return index else return -1
#Binary Search => check the middle element of the list and compare it with the target
#if the middle element is equal to the target, return the index of the middle element
#if the middle element is less than the target, search in the right half of the list
#if the middle element is greater than the target, search in the left half of the list
#Repeat the process until the target is found or the list is empty

import random
import time

def naive_search(arr , target):
    #example arr= [1, 2,3,4,5] , target = 3
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


#Bianry Search
def binary_search(arr , target , low= None , high = None):
    if low is None:
        low = 0
    if high is None:
        high = len(arr)-1

    if high < low:
        return -1    
    #example arr= [1, 2,3,4,5] , target = 3
    midpoint = (low + high) // 2
    if arr[midpoint] == target:
        return midpoint
    elif target > arr[midpoint]:
        return binary_search(arr , target , midpoint+1 , high)
    else:
        return binary_search(arr , target , low , midpoint-1)
    

if __name__ == "__main__":
    # arr = [1, 3 , 5, 10 ,12]
    # target = 10
    # print(naive_search(arr , target))
    # print(binary_search(arr , target))

    length = 10000
    sorted_list =set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length , 3*length))
    sorted_list = sorted(list(sorted_list)) 

    start   = time.time()
    for target in sorted_list:
        naive_search(sorted_list , target)

    end = time.time()
    print("Naive Search Time: " , (end - start)/length , "seconds")

    start   = time.time()
    for target in sorted_list:
        binary_search(sorted_list , target)

    end = time.time()
    print("Binary Search Time: " , (end - start)/length , "seconds")

    