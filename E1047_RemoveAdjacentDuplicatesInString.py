class Solution:
    def removeDuplicates(self, S: str) -> str:
        # stack 
        if len(S) <= 1:
            return S
        stack = []
        prev = None
        for ch in S:
            if not prev:
                prev = ch
                stack.append(ch)
            elif ch != prev:
                stack.append(ch)
                prev = ch
            elif ch == prev and stack[-1] == ch: # ch == prev
                stack.pop()
                # reset prev 
                prev = stack[-1] if stack != [] else None

        return ''.join(stack)
        
            