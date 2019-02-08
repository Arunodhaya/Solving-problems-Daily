
#Initial Template for Python 3
def isNeighbor(num):
    a = num % 10
    if  (10 - (10-a)) <= 2 or (10 - a) <= 2:
        return True
    else:
        return False
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        n=int(input())
        print(isNeighbor(n))
        testcases-=1
        
if __name__=='__main__':
    main()






