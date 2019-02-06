#Initial Template for Python 3
def inPutCat():
    a=input()##complete this
    b=input()##complete this
    c=input()##complete this
    print(a +" "+b+" "+ c) 
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        inPutCat() #the function that gets things done
        testcases-=1
        
if __name__=='__main__':
    main()
