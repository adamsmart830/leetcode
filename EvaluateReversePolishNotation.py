class Solution(object):
    def evalRPN(self, tokens):
        from collections import deque
        """
        :type tokens: List[str]
        :rtype: int

        Runtime: 20.23%
        Memory: 43.96%
        """
        stack = deque()
        for token in tokens:
            print(token)
            if token == '+':
                total = stack.pop()
                total += stack.pop()
            elif token == '*':
                total = stack.pop()
                total = int(stack.pop()) * total
            elif token == '/':
                total = stack.pop()
                nextPop = stack.pop()


                total = float(nextPop) / float(total) 

            elif token == '-':
                total = stack.pop()
                total = stack.pop() - total
            else:
                total = token
            stack.append(int(total))
          
        return stack.pop()
            