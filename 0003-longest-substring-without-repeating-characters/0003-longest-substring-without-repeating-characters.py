class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      start = max_length = 0
      letters = set()

      for end in range(len(s)):
        # If the end character is already in the set,
        # advance the start pointer.
        while s[end] in letters:
          letters.remove(s[start])
          start += 1

        # Now we can add the end character.
        letters.add(s[end])
        max_length = max(max_length, end - start + 1)
    
      return max_length