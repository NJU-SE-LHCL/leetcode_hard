# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        arr=[]
        for i in lists:
            while i:
                arr.append(i.val)
                i=i.next
        if arr==[]:
            return []
        arr.sort()
        ret=ListNode(0)
        head=ret
        i=0
        while i<len(arr):
            ret.next=ListNode(arr[i])
            ret=ret.next
            i+=1
        return head.next
