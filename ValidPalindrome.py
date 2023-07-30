class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        fast = len(s) - 1
        slow = 0

        while slow < fast:
            while slow < fast and not s[slow].isalnum():
                slow += 1
            while fast > slow and not s[fast].isalnum():
                fast-=1
            if(s[slow].lower() != s[fast].lower()):
                return False
            slow += 1
            fast -= 1
        
        return True

