class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = {}
        wordList = []
        res = []
        for word in words:
            count[word] = count.get(word, 0) + 1

        for word, freq in count.items():
            wordList.append((-freq, word))
            
        heapq.heapify(wordList)

        for _ in range(k):
            res.append(heapq.heappop(wordList)[1])

        return res
        

        