class Solution:
    def isValid(self, s: str) -> bool:
        queue = []

        for ch in s:
            if ch in ['(', '{', '[']
                queue.append(ch)
            else:
                if ch == ')' and (queue or [None])[-1] == '(':
                    queue.pop()
                elif ch == '}' and (queue or [None])[-1] == '{':
                    queue.pop()
                elif ch == ']' and (queue or [None])[-1] == '[':
                    queue.pop()
                else:
                    return False

        if not queue:
            return True
        else:
            return False