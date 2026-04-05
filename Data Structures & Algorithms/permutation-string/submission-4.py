class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False
        
        left = 0
        right = len(s1) - 1
        map1 = {}
        for char in s1:
            if char in map1:
                map1[char] += 1
            else:
                map1[char] = 1

        while right <= len(s2):
            sub_string = s2[left: right + 1]
            map2 = {}
            for char in sub_string: 
                if char in map2:
                    map2[char] += 1
                else:
                    map2[char] = 1
            
            if map1 == map2:
                return True
            right += 1
            left += 1
        
        return False
        





        