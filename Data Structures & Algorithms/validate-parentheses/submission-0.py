class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        close_to_open = {")": "(", "}": "{", "]": "["}
        for c in s:
            if c in close_to_open: # checks if it is a closing paranthesis
                if stk and stk[-1] == close_to_open[c]: # check if valid pairs
                    stk.pop()
                else:
                    return False # not matching brackets
            else: # open paranthesis
                stk.append(c)

        return len(stk) == 0