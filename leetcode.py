# 1207. Unique Number of Occurrences
"""Given an array of integers arr, return true if the number 
of occurrences of each value in the array is unique or false otherwise.

 

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1.
No two values have the same number of occurrences."""
from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}

        # Count frequency of each number
        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        # Check if frequencies are unique
        seen = set()
        for count in freq.values():
            if count in seen:
                return False
            seen.add(count)

        return True


# -------- Main Execution --------
if __name__ == "__main__":
    arr = [1, 2, 2, 1, 1, 3]   # sample input

    solution = Solution()
    result = solution.uniqueOccurrences(arr)

    print("Input Array:", arr)
    print("Unique Occurrences:", result)
# 344. Reverse String
"""Solved
Easy
Topics
premium lock icon
Companies
Hint
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 """
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


# -------- Main Execution --------
if __name__ == "__main__":
    s = ["h", "e", "l", "l", "o"]

    solution = Solution()
    solution.reverseString(s)

    print("Reversed String:", s)
"""Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7."""
class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}
        
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        
        length = 0
        odd_found = False
        
        for count in freq.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                odd_found = True
        
        if odd_found:
            length += 1
        
        return length
"""263. Ugly Number
Solved
Easy
Topics
premium lock icon
Companies
An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.

Given an integer n, return true if n is an ugly number.

 

Example 1:

Input: n = 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: n = 1
Output: true
Explanation: 1 has no prime factors.
Example 3:

Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes the prime factor 7."""