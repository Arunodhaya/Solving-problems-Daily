
#Initial Template for Python 3
def comparison(a,b):
    print(a==b) 
    print(a>b) 
    print(a!=b) 
    print(a<b) 
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        a=int(input())
        b=int(input())
        comparison(a,b)
        testcases-=1
        
if __name__=='__main__':
    main()



