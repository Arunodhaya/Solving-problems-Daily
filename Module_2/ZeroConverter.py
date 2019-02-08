def pos(n):
    
    while(n>0):
        print(n-1,end=" ")
        n-=1
def neg(n):
    
    while(n<=0):
        print(n,end=" ")
        n+=1
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        numbah=int(input())
        if(numbah>0):
            pos(numbah)
        elif(numbah<0):
            neg(numbah)
        else:
            print("already Zero",end="")
        print()
        testcases-=1
        
if __name__=='__main__':
    main()


