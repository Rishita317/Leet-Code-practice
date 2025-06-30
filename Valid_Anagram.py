# 242. Valid Anagram
# Easy
# Topics
# premium lock icon
# Companies
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Defination: a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.
# note if there is an addition of a new words its not considred an anagram ( example 2)
 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

# SOLUTION

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sMap = {}
        # fill sMap with letters from s
        for letter in s:
            sMap[letter] = sMap.get(letter, 0) + 1

        tMap = {}
        # fill tMap with letters from t
        for letter in t:
            tMap[letter] = tMap.get(letter, 0) + 1

        if sMap == tMap:
            return True
        else:
            return False
