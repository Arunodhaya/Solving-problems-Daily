def inPutS():
    a=input()
    s,i,f = a.split(' ') 
    sum=int(i)+float(f)
    print(s+" "+str(sum))

def main():
    testcases=int(input())
    while(testcases>0):
        inPutS() 
        testcases-=1
        
if __name__=='__main__':
    main()



