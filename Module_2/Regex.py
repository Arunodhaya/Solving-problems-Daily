
#Initial Template for Python 3
import re ##import re module to use regex
def numberMatcher(str):
    pat=re.compile('\d+')##write the pattern here
    match=pat.findall(str)##find all finds all the matched texts and returns a list
    # print(pat.findall(str))
    if(match): 
         for i in match:
             print(i, end=" ")
    else:
         print(-1,end="")
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        mystr=input()
        numberMatcher(mystr)
        print()
        testcases-=1
        
if __name__=='__main__':
    main()


