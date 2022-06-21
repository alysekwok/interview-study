
# Given the string, check if it is a palindrome.



def solution(inputString):
    if len(inputString) == 1:
        return True
    count = len(inputString)-1
    for char in range(int(len(inputString)/2)):
        if inputString[char] != inputString[count]:
            return False
        count = count - 1
    return True