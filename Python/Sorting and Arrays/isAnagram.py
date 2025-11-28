'''
Given two strings s and t, return true if the two strings are anagrams of each other,
otherwise return false.

An anagram is a string that contains the exact same characters as another string, 
but the order of the characters can be different.

Example 1:
Input: s = "racecar", t = "carrace"
Output: true

NOTE: 
    Below uses O(1) space by pre creating the alphabets list
    ord(char) - ord('a') gives a number from 0 - 25
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        alphabets = [0] * 26

        for letter in s:
            alphabets[ord(letter) - ord('a')] += 1

        for letter in t:
            alphabets[ord(letter) - ord('a')] -= 1

        for letter in alphabets:
            if letter != 0:
                return False
        
        return True
