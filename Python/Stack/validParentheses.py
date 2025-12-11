class Solution:
    def isValid(self, s: str) -> bool:
        # map to add closer to stack
        parMap = {'(': ')', '[': ']', '{': '}'}
        stack = []
        # iterate each bracket
        for p in s:
            # if an opener, push
            if p in parMap:
                stack.append(parMap[p])
            # if closer:
            else:
                # if not empty and last in matches -> correct order
                if len(stack) != 0 and stack[-1] == p:
                    stack.pop()
                else:
                    return False
        # if not empty -> not valid
        if len(stack) != 0: return False
        return True
