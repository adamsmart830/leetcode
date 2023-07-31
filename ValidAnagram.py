class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dictionary = {}
        for char in s:
            if char in dictionary:
                dictionary[char] += 1
            else:
                dictionary[char] = 1
        

        for char in t:
            if char in dictionary:
                dictionary[char] -= 1
                if dictionary[char] < 0:
                    #print("Rrere")
                    return False
            else: 
                #print("Rrereasdsadas")
                return False
        
        for char in s:
            if dictionary[char] != 0:
                return False

        return True