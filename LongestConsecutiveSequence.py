class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hs = set(nums)
        longest = 0
        for n in nums:
            if n - 1 not in hs:
                length = 1
                while n + length in hs:
                    length +=1
                longest = max (longest, length)


        return longest
            
            
