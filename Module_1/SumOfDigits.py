#Initial Template for Python 3
def digitsSum(n):
    ##Your code here
    sum=0
    rem=0
    while(n>0):
        rem=n%10
        sum=sum+rem
        n=n//10
    return sum
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        a=int(input())
        print(digitsSum(a))
        testcases-=1
        
if __name__=='__main__':
    main()


