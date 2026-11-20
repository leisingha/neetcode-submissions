class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        seq = []
        for i in numsSet:
            if (i-1) not in numsSet:
                seq.append(i)
        longest = 0
        for start in seq:
            length = 1
            while (start+length) in numsSet:
                length+=1
            longest = max(longest, length)
        return longest
        
                
                



            

        