class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        start=0
        maxans=0
        stack=[]
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            else:
                if len(stack)==0:
                    start=i+1
                    continue
                else:
                    a=stack.pop()
                    if len(stack)==0:
                        maxans=max(i-start+1,maxans)
                    else:
                        maxans=max(i-stack[-1],maxans)
        return maxans


if __name__=='__main__':
    a=Solution()
    s="(()()"
    print (a.longestValidParentheses(s))
                
            