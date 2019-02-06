
#Initial Template for Python 3
def do_operation(x, y):
    # Your code here
    x-=1
    y+=1
    print (x)
    print (y)
# Driver code
def main():
    testcase = int(input())
    
    while(testcase > 0):
        input1 = input().split()
        x = int(input1[0])
        y = int(input1[1])
        do_operation(x, y)
        testcase -= 1
        
if __name__ == '__main__':
    main()


