#User function Template for python3

from typing import List

class Solution:
    def reverse(self,St): 
        #code here
        if len(St) == 0 :
            return
        temp = St.pop()
        self.reverse(St)
        self.insertStack(St,temp)
        return St
        
    def insertStack(self , St , temp) :
        if len(St) == 0:
            St.append(temp)
            return
        val = St.pop()
        self.insertStack(St,temp)
        St.append(val)

#{ 
 # Driver Code Starts

#Initial Template for Python 3

 
for _ in range(int(input())):
    N = int(input())
    St = list(map(int, input().split()))
    ob = Solution()
    ob.reverse(St)
    print(*St)
    print("~")
# } Driver Code Ends