
#Initial Template for Python 3
def do_operation(x, y):
    # Your code here
    print(x+y)
    print(x-y)
    print(x*y)
    print(x/y)
    print(x**y)
    print(x//y)
# Python Code to perform mathematical operation
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
    
