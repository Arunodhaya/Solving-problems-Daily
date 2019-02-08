
#Initial Template for Python 3
def printIncreasingPower(x):
    ##Your code here
    a=1
    sq=0
    while (sq < x):
        sq=a * a
        if sq>x:
            break
        print (sq,end=" ")
        
        a += 1
    
    
        
         
        ##Your code here
# Driver Code
def main():
    # Testcase input
    testcases = int(input())
    
    
    # Looping through testcases
    while(testcases > 0):
        x = int(input())
        
        printIncreasingPower(x);
        print ()
        
        
        testcases -= 1
 
if __name__ == '__main__':
    main()


