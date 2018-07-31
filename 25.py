# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def list2arr(x):
            ret_arr=[]
            while x:
                ret_arr.append(x.val)
                x=x.next
            return ret_arr
        arr=list2arr(head)
        length = len(arr)
        #print (length)
        flag = 0
        if length % k:
            flag = 1
        time = int(length/k)
        '''
        print('time:')
        print (time)
        '''
        fin_list = ListNode(0)
        ans_list=fin_list
        for i in range(time):
            #print (i)
            for j in reversed(range(i*k,i*k+k)):
                #print (j)
                fin_list.next=ListNode(arr[j])
                fin_list=fin_list.next
        if flag:
            for i in range(time*k,length):
                fin_list.next=ListNode(arr[i])
                fin_list=fin_list.next
        return ans_list.next



if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    k = 2
    def arr2list(x):
        ret_list = ListNode(0)
        head=ret_list
        #length = len(x)-1
        while x:
            ret_list.next = ListNode(x.pop(0))
            ret_list = ret_list.next
        return head.next
    test_list=arr2list(arr)
    a=Solution()
    res_list=a.reverseKGroup(test_list,k)
    while res_list:
        print(res_list.val)
        #print ('上班')
        res_list=res_list.next
