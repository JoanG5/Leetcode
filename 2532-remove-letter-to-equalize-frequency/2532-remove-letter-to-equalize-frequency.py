class Solution(object):
    def equalFrequency(self, word):
        counter = Counter(Counter(word).values())

        if len(counter) == 1: 
            return 1 in counter or 1 in counter.values()

        if len(counter) == 2:
            return counter[1] == 1 or counter[min(counter) + 1] == 1
        
        return False
                
        
        

               