Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?


Solution:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if lengths are different
        if len(s) != len(t):
            return False
        
        # Initialize a dictionary to store character counts
        char_count = {}
        
        # Count characters in string s
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Decrement character counts for string t
        for char in t:
            if char not in char_count:
                return False
            char_count[char] -= 1
            if char_count[char] < 0:
                return False
        
        # Check if all counts are zero
        return all(count == 0 for count in char_count.values())

# Example usage:
solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))  # Output: True
print(solution.isAnagram("rat", "car"))          # Output: False
