
#Initial Template for Python 3
power = lambda a,b:a**b    
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        base=int(input())
        exp=int(input())
        print(power(base,exp)) ##calling the anonymous function
        testcases-=1
        
if __name__=='__main__':
    main()



    
