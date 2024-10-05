class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        largest = -1
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i] 
            arr[i] = largest
            if temp > largest:
                largest = temp 
        
        return arr