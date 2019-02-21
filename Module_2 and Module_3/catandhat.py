def cat_hat(str):
    
    c_count=0
    h_count=0
    for i in range(0,len(str)-2):
        if str[i]=='c' and str[i+1]=='a' and str[i+2]=='t':
            c_count+=1
        if str[i] == 'h'and str[i+1]=='a' and str[i+2]=='t':
            h_count+=1

    if c_count == h_count:
        return True
    else:
        return False


def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        mystr=input()
        print(cat_hat(mystr))
        testcases-=1
        
if __name__=='__main__':
    main()



