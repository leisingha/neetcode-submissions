class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        sequence_starters = []
        for i in num_set:
            if (i-1) not in num_set:
                sequence_starters.append(i)
        
        max_length = 0
        for num in sequence_starters:
            counter = 1
            while (num+1) in num_set:
                counter += 1
                num += 1
                
            if counter > max_length:
                max_length = counter
        return max_length



        
                
                



            

        