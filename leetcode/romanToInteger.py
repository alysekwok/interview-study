# Given a roman numeral, convert it to an integer.


hashmap = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900
}

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        length = 0
        while length < len(s):
            if length + 1 < len(s) and s[length] + s[length + 1] in hashmap:
                total += hashmap[s[length] + s[length + 1]]
                length += 2
            else:
                total += hashmap[s[length]]
                length += 1
        return total