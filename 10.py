class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def isequal(char1,char2):
            if char1=='.' or char2=='.':
                return True
            elif char1==char2:
                return True
            else:
                return False
        if p=="":
            return bool(s=="")
        if len(p)>1 and p[1]=='*':
            return bool(self.isMatch(s,p[2:]) or (s and isequal(s[0],p[0]) and self.isMatch(s[1:],p)))
        else:
            return bool(s and isequal(s[0],p[0]) and self.isMatch(s[1:],p[1:]))

if __name__ == '__main__':
    s = Solution()
    print(s.isMatch("ab", ".*c"))  # false
    print(s.isMatch("aa", "aa"))  # true
    print(s.isMatch("aaa", "aa"))  # false
    print(s.isMatch("aa", "a*"))  # true
    print(s.isMatch("aa", ".*"))  # true
    print(s.isMatch("ab", ".*"))  # true
    print(s.isMatch("aab", "c*a*b"))  # true