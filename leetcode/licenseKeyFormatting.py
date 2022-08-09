# You are given a license key represented as a string s that consists of only alphanumeric characters 
# and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.

# We want to reformat the string s such that each group contains exactly k characters, except for 
# the first group, which could be shorter than k but still must contain at least one character. 
# Furthermore, there must be a dash inserted between two groups, and you should convert all 
# lowercase letters to uppercase.

# Return the reformatted license key.

def licenseKeyFormatting(s, k):
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    newS = s.upper()
    string = ""
    result = ""
    for char in newS:
        if char.isalpha() or char.isdigit():
            string += char
    string = string[::-1]
    for num in range(len(string)):
        if num % k == 0 and num != 0:
            result = result + "-" + string[num]
        else:
            result += string[num]
    print(result[::-1])
    return result[::-1]

s = "5F3Z-2e-9-w"
k = 4  
licenseKeyFormatting(s,k) 
s1 = "2-5g-3-J"
k1 = 2
licenseKeyFormatting(s1,k1) 
s2 = "a-a-a-a-"
k2 = 1
licenseKeyFormatting(s2,k2) 

