
sum = lambda x,y:x+y
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        x=int(input())
        y=int(input())
        
        print(sum(x,y))
        
        testcases-=1
        
if __name__=='__main__':
    main()


