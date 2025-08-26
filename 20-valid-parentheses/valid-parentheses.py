class Solution:
    def isValid(self, s: str) -> bool:
        # If there had been more than 3 possible characters, I would have used a dictionary to 
        # reduce the amount of logic and duplicate code that this solution uses.
        stack = []

        for i in range(len(s)):

            # Opening Brackets
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])

            # Closing Brackets
            elif s[i] == ')':
                if not stack:
                    return False
                else:
                    closeBracket = stack.pop()
                    if closeBracket != '(':
                        return False
            elif s[i] == ']':
                if not stack:
                    return False
                else:
                    closeBracket = stack.pop()
                    if closeBracket != '[':
                        return False                    
            elif s[i] == '}':
                if not stack:
                    return False
                else:
                    closeBracket = stack.pop()
                    if closeBracket != '{':
                        return False
            else:
                return False
        
        if len(stack) > 0:
            return False

        return True