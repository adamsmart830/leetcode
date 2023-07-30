class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """



        l = 0 
        r = len(numbers) - 1

        while(l < r):
            t = numbers[l] + numbers[r]
            if(t == target):
                return l + 1, r + 1

            if t > target:
                r-=1
            if t < target:
                l+=1
            
            
                