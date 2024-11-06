class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Ignore leading zeros
        # Compare the cur sections version with the other
        # if one version ends early then its val can be replaced with  0

        a = b = 0
        
        while a < len(version1) or b < len(version2):
            num1 = num2 = 0

            while a < len(version1) and version1[a] != ".":
                num1 = (num1 * 10) + int(version1[a])
                a += 1
            
            while b < len(version2) and version2[b] != ".":
                num2 = (num2 * 10) + int(version2[b])
                b += 1
            
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
            a += 1
            b += 1
            
        return 0
            