class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if s=="" or words==[]:
            return []
        wordlength=len(words[0])
        wordslength=len(words)
        slength=len(s)
        wordmap={}
        tmpmap={}
        ans_list=[]
        for i in words:
            if i not in wordmap:
                wordmap[i]=1
            else:
                wordmap[i]+=1
        print (wordmap)
        for i in range(slength-wordlength*wordslength+1):
            #print (i)
            if s[i:i+wordlength] in wordmap:
                for j in range(wordslength):
                    st=i+j*wordlength
                    ed=i+(j+1)*wordlength
                    tmp=s[st:ed]
                    #print (tmp)
                    if tmp in wordmap:
                        if tmp not in tmpmap:
                            tmpmap[tmp]=1
                        else:
                            tmpmap[tmp]+=1
                        if tmpmap[tmp]>wordmap[tmp]:
                            #print ('stop')
                            break
                    else:
                        break
                    if j==wordslength-1:
                        ans_list.append(i)
                #print (tmpmap)
                tmpmap.clear()
        return ans_list


if __name__=='__main__':
    a=Solution()
    s = "wordgoodgoodgoodbestword"
    words = ["word","good","best","good"]
    xans=a.findSubstring(s,words)
    print (xans)

