class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # act ==  cat in sorted
        # map of words who matches with the sorted letters 

        map = {}
        for str in strs:
            sortedWord = "".join(sorted(str))
            if sortedWord in map:
                map[sortedWord].append(str)
            else:
                map[sortedWord] = [str]
        
        result = []
        for list in map:
            result.append(map[list])

        return result
