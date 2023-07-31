class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        dicta = {}
        for string in strs:
            ct = 1
            for chars in string:
                ct *= hash(chars)
                
            
            if ct not in dicta:
                dicta[ct] = []
            
            dicta[ct].append(string)


        my_list = list(dicta.values())
        return my_list
            
