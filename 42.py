class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height==[]:
            return 0
        ans=0
        '''预处理很重要'''
        length=len(height)
        leftmax=[0]*length
        rightmax=[0]*length
        cur=0
        for i in range(length):
            leftmax[i]=cur
            cur=max(height[i],cur)
        cur=0
        for i in reversed(range(length)):
            rightmax[i]=cur
            cur=max(height[i],cur)
        print (leftmax)
        print (rightmax)
        for i in range(1,length-1):
            tmp=min(leftmax[i],rightmax[i])
            if tmp>height[i]:
                ans+=tmp-height[i]
            #print ("i,tmp:",i,tmp)
        return ans

