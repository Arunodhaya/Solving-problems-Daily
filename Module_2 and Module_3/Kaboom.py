
#Initial Template for Python 3
def boom(str):
    ##Your code here
    return(str.endswith('boom'))
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        str=input()
        print(boom(str))
        testcases-=1
        
if __name__=='__main__':
    main()

