class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dicta = {}
        for num in nums:
            if num not in dicta:
                dicta[num] = 0
            dicta[num] += 1


        l = (sorted(dicta.items(), key=lambda x:x[1], reverse=True))
        
        arr = []
        for x in range(k):
            arr.append(l[x][0])
        return arr
        

        