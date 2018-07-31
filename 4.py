class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m=len(nums1)
        n=len(nums2)
        z=int((n+m+1)/2)
        flag=(n+m)%2
        if m>n:
            nums1,nums2,m,n=nums2,nums1,n,m
        lo=0
        hi=m
        while lo<=hi:
            i=int((lo+hi)/2)
            j=z-i
            if i<m and nums1[i]<nums2[j-1]:
                lo+=1
            elif i>0 and nums1[i-1]>nums2[j]:
                hi-=1
            else:
                if i==0:
                    left=nums2[j-1]
                elif j==0:
                    left=nums1[i-1]
                else:
                    left=max(nums1[i-1],nums2[j-1])
                if flag:
                    return left
                if i==m:
                    right=nums2[j]
                elif j==n:
                    right=nums1[i]
                else:
                    right=min(nums1[i],nums2[j])
                return (left+right)/2.0


