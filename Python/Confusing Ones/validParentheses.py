'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order. NOTE: beware of conditions
Every close bracket has a corresponding open bracket of the same type.'''
class Solution:
    def isValid(self, s: str) -> bool:

        # odd length = at least one not closed
        if len(s) % 2 != 0: return False

        # map the opening brackets to its closing ones
        stack = []
        mapping = {'(': ')', '[': ']', '{': '}'}

        for st in s:

            # if the character is one of the openers, add to stack
            if st in mapping.keys():
                stack.append(st)
            else:

                # if stack is empty but character is a closer, then false
                if not stack: return False
                else:

                    # pop the last opening bracket from the stack
                    # check if its matching closing bracket is the same as the current character
                    # if not, parentheses are mismatched
                    if st != mapping.get(stack.pop()):
                        return False

        # if none in stack, all parentheses are closed            
        return len(stack) == 0