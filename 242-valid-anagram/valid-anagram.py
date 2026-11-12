class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequency = {}
        for ch in s:
            if ch in frequency:  
                frequency[ch] += 1
            else:
                frequency[ch] = 1
        for ch in t:
            if ch not in frequency:
                return False

            frequency[ch] -= 1

            if frequency[ch] < 0:
                return False

        for ch in frequency:
            if frequency[ch] != 0:
                return False
                
        return True                   

        