class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for c in s:
            if c == ')' or c == '}' or c == ']':
                if len(stack) == 0 or stack.pop() != c:
                    return False
            else:
                if c == '(':
                    stack.append(')')
                elif c == '{':
                    stack.append('}')
                elif c == '[':
                    stack.append(']')
        
        if len(stack) == 0:
            return True
        else:
            return False
            
