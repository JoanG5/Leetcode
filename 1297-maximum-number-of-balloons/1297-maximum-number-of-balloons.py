class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = {}
        for i in text:
            if i in ["b", "a", "l", "l", "o", "o", "n"]:
                counter[i] = counter.get(i, 0) + 1
        
        count = 0
        while True:
            for letter in "balloon":
                if letter not in counter or counter[letter] == 0:
                    return count
                counter[letter] -= 1
            count += 1
    