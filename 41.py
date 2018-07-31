class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict_num={}
        minnum=pow(2,31)-1
        maxnum=-1
        for i in nums:
            if i>0:
                minnum=min(minnum,i)
                maxnum=max(maxnum,i)
                dict_num[str(i)]=1
        if minnum>1:
            return 1
        else:
            ret=minnum+1
            flag=1
            while flag:
                if str(ret) in dict_num:
                    ret+=1
                else:
                    break
            return ret


if __name__=='__main__':
    a=Solution()
    list=[1,2,0]
    print (a.firstMissingPositive(list))