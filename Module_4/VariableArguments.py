def multivar(a, *var): 
    ##*var takes multiple arguments inside it
    ##print the sum of a+elements of var
    
    ar = sum(i for i in var)
    s = ar+a
    print(s)
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        single=int(input())
        multivar(single,4,5,6,7) ## The single argument and multiarguments are passed to multivar function
        testcases-=1
        
if __name__=='__main__':
    main()


