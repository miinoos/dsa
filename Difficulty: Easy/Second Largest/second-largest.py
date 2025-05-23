#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        max = arr[0]
        secondMax = arr[0]
        for i in range(len(arr)) :
            if(max < arr[i]) :
                secondMax = max
                max = arr[i]
            elif(arr[i] > secondMax) and (arr[i]<max) :
                secondMax = arr[i]
            elif(arr[i] < secondMax) and (secondMax == max) :
                secondMax = arr[i]
        
        if(secondMax == max) :
            return -1
        
        return secondMax


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends