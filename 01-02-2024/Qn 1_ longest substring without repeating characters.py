Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.


Solution:

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        
        # Initialize a dictionary to store the index of each character
        char_index = {}
        max_length = 0
        start = 0
        
        for end in range(n):
            if s[end] in char_index and char_index[s[end]] >= start:
                # If the character is repeated, update the start index
                start = char_index[s[end]] + 1
            
            # Update the index of the current character
            char_index[s[end]] = end
            
            # Update the maximum length
            max_length = max(max_length, end - start + 1)
        
        return max_length

# Example usage:
solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
print(solution.lengthOfLongestSubstring("bbbbb"))     # Output: 1
print(solution.lengthOfLongestSubstring("pwwkew"))    # Output: 3
