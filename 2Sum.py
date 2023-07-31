class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dicta = {}
        ct = 0
        for num in nums:
            if num in dicta:
                return dicta[num], ct
            complement = target - num
            dicta[complement] = ct
            ct+=1