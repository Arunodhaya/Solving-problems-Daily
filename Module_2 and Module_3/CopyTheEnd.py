
#Initial Template for Python 3
def copyCat(str):
    ##Your code here
    st = str[-2:]
    return st+st+st
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        str=input()
        print(copyCat(str))
        testcases-=1
        
if __name__=='__main__':
    main()


