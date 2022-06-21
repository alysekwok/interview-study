
# Given an array of integers, find the pair 
# of adjacent elements that has the largest product
# and return that product.

def solution(inputArray):
    maxSum = -100000
    if len(inputArray) == 2:
        return inputArray[0] * inputArray[1]
    for num in range(len(inputArray)-1):
        product = inputArray[num] * inputArray[num + 1]
        maxSum = max(product, maxSum)
    return maxSum