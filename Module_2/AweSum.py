
#Initial Template for Python 3
def aweSum(a, b):
    ##Your code here
    sum = a+b
    if sum in range(20,41):
       return 42
    else:
       return sum
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        a=int(input())
        b=int(input())
        print(aweSum(a,b))
        testcases-=1
        
if __name__=='__main__':
    main()


