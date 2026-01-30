class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = float('-inf')
        curs = 0
        for num in nums:
            curs += num
            maxsum = max(maxsum,curs)
            if curs<0:
                curs=0
        return maxsum
    
        