
import re
def validate(str):
    pat= re.compile(r'[a-z]+\W+\d') ##your pattern here
    match=pat.search(str)
    if(match):
        return True
    else:
        return False
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        mystr=input()
        print(validate(mystr))
        testcases-=1
        
if __name__=='__main__':
    main()

