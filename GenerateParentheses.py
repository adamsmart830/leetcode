class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]

        Runtime: 87.97%
        Memory: 58.91%
        """
        stack = []
        result = []

        def backTrack(l, r):
            if l == r == n:
                result.append(''.join(stack))
                return
            if l < n:
                stack.append('(')
                backTrack(l + 1, r)
                stack.pop()
            if r < l:
                stack.append(')')
                backTrack(l, r + 1)
                stack.pop()

        backTrack(0, 0)
        return result
            