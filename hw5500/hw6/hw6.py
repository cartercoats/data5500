'''
Easy: (3 points)

1. Given an array of integers, write a function to calculate the sum of all elements in the array.

Analyze the time complexity of your solution using Big O notation, especially what is the Big O notation
of the code you wrote, and include it in the comments of your program
'''
import array
nums = array.array('i',[42,12,553,64,5])

def sum_array(arr):
    total = 0
    for num in arr:
        total += num
    print('Sum:',total)

sum_array(nums)

# The loop is going to iterate though each value in nums. That makes it O(n)


'''
Medium: (5 points)

2. Given an array of integers, write a function that finds the second largest number in the array.

Analyze the time complexity of your solution using Big O notation, especially what is the Big O notation
of the code you wrote, and include it in the comments of your program.
'''

def second_largest(arr):
    largest = 0
    second = 0
    for num in arr:
        if num > largest:
            largest = num
    for num in arr:
        if num > second and num < largest:
            second = num
    print('Second Largest Number:',second)

second_largest(nums)

# The function is 2 loops but they are not nested, so big O notation is O(n)
'''
Hard: (7 points)

3. Write a function that takes an array of integers as input and returns the maximum
difference between any two numbers in the array.

Analyze the time complexity of your solution using Big O notation, especially what is
the Big O notation of the code you wrote, and include it in the comments of your program.
'''
def find_max_diff(arr):
    max_diff = 0
    for num in arr:
        for num2 in arr:
            diff = (num - num2)
            if diff > max_diff:
                max_diff = diff
    print('Maximum Difference:',max_diff)

find_max_diff(nums)
# This function has a for loop inside a for loop so Big O is O(n^2)
# This particular array has 5 values, so that's 5 opererations 5 times totalin 25 operations