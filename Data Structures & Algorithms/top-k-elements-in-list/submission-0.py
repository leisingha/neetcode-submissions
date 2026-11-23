from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        vals = Counter(nums).most_common(k)
        result = []
        for item in vals:
            result.append(item[0])
        return result
