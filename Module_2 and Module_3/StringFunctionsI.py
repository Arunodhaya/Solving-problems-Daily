
def trim(str):
    return str.lstrip(' ')    
def exists(str,istr):
    return str.find(istr)     
def titleIt(str):
    return str.title()    
def casesSwap(str):
    return str.swapcase()     

def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        mystr=input()
        x=input()
        mystr=trim(mystr)
        print(mystr)
        print(exists(mystr,x))
        print(titleIt(mystr))
        print(casesSwap(mystr))
        testcases-=1
        
if __name__=='__main__':
    main()


