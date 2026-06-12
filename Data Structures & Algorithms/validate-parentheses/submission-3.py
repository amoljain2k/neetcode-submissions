class Solution:
    def isValid(self, s: str) -> bool:
        stack= []
        close_to_open = {
            ")":"(",
            "]":"[",
            "}": "{"
        }
        for item in s:
            if item in close_to_open.values():
                stack.append(item)
            else:
                if stack and stack[-1]==close_to_open[item]:
                    stack.pop()
                else:
                    return False
        return not stack