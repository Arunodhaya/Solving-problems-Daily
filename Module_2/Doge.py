
#Initial Template for Python 3
def doge_count(str):
    count=0
    for one in range(97,123):
        li = [chr(one)]
    for i in range(len(str)-3):
        if str[i]=='d' and str[i+1]=='o' and any(str[i+2])==True and str[i+3]=='e':
           count+=1
    return count
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        str=input()
        print(doge_count(str))
        testcases-=1
        
if __name__=='__main__':
    main()


