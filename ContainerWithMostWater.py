class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        max_v = 0
        while l < r:
            total = min(height[l], height[r]) * (r - l)
            if total > max_v:
                max_v = total
            
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
            
        return max_v
