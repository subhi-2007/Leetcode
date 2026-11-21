class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        frequency={}
        for ch in magazine:
            if ch in frequency:
                frequency[ch]+= 1
            else:
                frequency[ch] = 1
        for ch in ransomNote:
            if ch not in frequency:
                return False
            frequency[ch] -= 1

            if frequency[ch] < 0:
                return False
        return True                        