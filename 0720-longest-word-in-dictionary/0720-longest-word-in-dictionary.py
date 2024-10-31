class Solution:
    def longestWord(self, words: List[str]) -> str:
        #make set with words, sort, and try to get parts in set
        wordSet = set(words)
        words.sort(reverse=True)
        res=""

        for word in words:
            valid = True
            for i in range(len(word) - 1):
                if not word[:i + 1] in wordSet:
                    valid = False
                    break
            if valid:
                if len(res) < len(word):
                    res = word
                elif len(res) == len(word):
                    res = min(res, word)

        return res