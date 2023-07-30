class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        print(nums)
        a = 0
        arr0 = []
        for num in nums:
            target = 0 - num
            l = a + 1
            r = len(nums) - 1
            while l < r:
                t = nums[l] + nums[r]
                if t == target:
                    arr = [num, nums[l], nums[r]]
                    arr.sort()
                    if arr not in arr0:
                        arr0.append(arr)
                    l+=1
                    continue
                if t > target:
                    r-=1  
                if t < target:
                    l+=1
                
                
            a += 1

        return arr0