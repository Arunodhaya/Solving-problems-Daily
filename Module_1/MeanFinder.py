
#Initial Template for Python 3
def mean(d,m):
    m=m*3
    mean=round((d+m)/4)
    return mean
    
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        d=int(input()) ##taking d as input
        m=int(input()) ## taking mean of 3 numbers
        print(mean(d,m))
        testcases-=1
        
if __name__=='__main__':
    main()


