
#Initial Template for Python 3
def print_elements(n, arr):
    # l = len(arr)//2
    # li = []
    # li1 = []
    
    # # Your code here 
    # # use '//' to divide to get int for index
    # for i in range(1,l+2):
    #     li.append(int(i))
    # for i in range(l+1,len(arr)+1):
    #     li1.append(int(i))    
    #     if len(li1)>3:
    #       li.append(li1[3])
    # print(li,end=" ")
    for i in range(0,n//2):
        print(arr[i],end=" ")  
    for i in range(n//2,n,3):
        print(arr[i],end=" ")
# Driver Code
def main():
    
    # Testcase input
    testcases = int(input())
    
    # Looping through testcases
    while(testcases > 0):
        # size of array
        size_array = int(input())
        
        # array elements input
        array = input().split()
        # print (array)
        arr = list()
        for i in array:
            arr.append(int(i))
            
        # print (arr)
        
        # calling function to print elements
        print_elements(size_array, arr)
        print ()
        testcases -= 1
 
if __name__ == '__main__':
    main()


