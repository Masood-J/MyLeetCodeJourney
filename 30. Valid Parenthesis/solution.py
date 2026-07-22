class Solution:
    def isValid(self, s: str) -> bool:


        stack=list()

        translateDict = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:


            if char in translateDict:

                if not stack or stack[-1]!=translateDict[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)


        return len(stack)==0

            
        