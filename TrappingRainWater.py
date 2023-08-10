class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int

        Runtime: 92.38% 
        Memory:  48.25%
        """

        
        l = 0
        max_left = height[l]

       
        r = len(height) - 1
        max_right = height[r]

        total = 0 
        while l < r:
           
            if max_left <= max_right:    
                l += 1
                max_left = max(max_left, height[l])
                total += max_left - height[l]


                
                
                

            else:
                r -= 1 
                max_right = max(max_right, height[r])
                total += max_right - height[r]
            
                
                
        
        return total