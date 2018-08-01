class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo=hi=step=0
        while hi<len(nums)-1:
            lo,hi=hi+1,max(i+nums[i] for i in range(lo,hi+1))
            step+=1
        return step

if __name__=='__main__':
    a=Solution()
    print (a.jump([2,3,1,1,4]))