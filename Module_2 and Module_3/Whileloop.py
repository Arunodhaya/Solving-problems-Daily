#Initial Template for Python 3
def printInDecreasing(x):
    # Complete the code below
    while(x >= 0):
        print(x, end=" ")
        x -= 1
# Driver Code
def main():
    
    # Testcase input
    testcases = int(input())
    
    # Looping through testcases
    while(testcases > 0):
        x = int(input())
        
        printInDecreasing(x);
        
        print ()
        
        testcases -= 1
 
if __name__ == '__main__':
    main()



        
