class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        """
        Find the larger version of each section, ie the numbers inbetween .
        Ignore leading zeros until a dif number is found 
        Once digit != 0 on both sides line them up
        Start comparing until a . is reached or a differnce is found
        Continue this until a difference is found 

        Issues with numbers of difernt lengths
        Replace it with 0
        """
        a = b = 0

        while a < len(version1) or b < len(version2):
            num1 = num2 = 0
            while a < len(version1) and version1[a] != '.':
                num1 = 10 * num1 + int(version1[a]) 
                a += 1
            while b < len(version2) and version2[b] != '.':
                num2 = 10 * num2 + int(version2[b]) 
                b += 1
            if num1 > num2: return 1
            elif num2 > num1: return -1
            a += 1
            b += 1
        return 0
            