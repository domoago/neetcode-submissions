class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }
        for parenthesy in s:
            if parenthesy in closeToOpen:
                if stack and stack[-1] == closeToOpen[parenthesy]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(parenthesy)
        return True if not stack else False