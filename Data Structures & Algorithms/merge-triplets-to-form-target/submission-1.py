class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # one of the triplet number should be in ith candidate
        # Input: triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]], target = [5,5,5]
        # [[2,5,4], [2,3,4], [1,2,5], [5,2,3]]
        # [[2,5,4], [1,2,5], [5,2,3]]
        # [[2,5,5], [5,2,3]]
        # [5,5,5] <-- target

        while len(triplets) > 1:
            first_tri = triplets[0]
            second_tri = triplets[1]

            # do element wise comparision btw first_tri with target tri, if
            # any element is bigger, we can discard that triplet
            if (first_tri[0] > target[0] or first_tri[1] > target[1] or first_tri[2] > target[2]):
                triplets.pop(0)
                continue
            if (second_tri[0] > target[0] or second_tri[1] > target[1] or second_tri[2] > target[2]):
                triplets.pop(1)
                continue
            
            # merge them and insert into triplets
            merged = [max(first_tri[0], second_tri[0]), max(first_tri[1], second_tri[1]), max(first_tri[2], second_tri[2])]
            triplets.pop(0)
            triplets.pop(0)
            
            # check if merged become the target
            if (merged[0] == target[0] and merged[1] == target[1] and merged[2] == target[2]):
                return True
            
            triplets.append(merged)
        
        return (triplets[0][0] == target[0] and triplets[0][1] == target[1] and triplets[0][2] == target[2])


            