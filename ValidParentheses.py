class Solution(object):
    from collections import deque
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool

        Runtime: 99.71%
        Memory: 79.99%
        """
        stack = deque()


        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '{':
                stack.append('}')
            elif c == '[':
                stack.append(']')

            elif len(stack) > 0:
                if c != stack.pop():
                    return False
            else:
                return False
            
        print(stack)
        if len(stack) != 0:
            return False

        return True