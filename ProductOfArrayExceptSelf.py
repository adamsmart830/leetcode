class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = 1
        output = [0] * len(nums)
        ct = 0
        while ct < len(nums):
            output[ct] = prefix
            prefix *= nums[ct]
            ct+=1
        #print(output)
        
        postfix = 1
        ct -=1
        #print(ct)
        while ct >= 0:
            output[ct] *= postfix
            postfix *= nums[ct]
            ct-=1
        
        return output
