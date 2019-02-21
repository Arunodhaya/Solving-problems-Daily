
#Initial Template for Python 3
def isPrime(n):
    for i in range(2,int(math.sqrt(n))):
            if n%i==0:
               return False
            else:  
               return True
import math ##You will need this for prime checking
    
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        number=int(input())
        print(isPrime(number)) ##This isPrime is function that you need to create
        testcases-=1
        
if __name__=='__main__':
    main()


