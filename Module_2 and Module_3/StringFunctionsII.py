
#Initial Template for Python 3

def gfg(a):
    b = a.lower()
    if(b.startswith('gfg')and(b.endswith('gfg'))):  # use b.startswith() and b.endswith()
        print ("Yes")
    else:
        print ("No")
# Driver Code
def main():
    # testcase input
    testcases = int(input())
    
    # looping through testcases
    while(testcases > 0):
        string = input()
        
        testcases -= 1
        
        gfg(string)
if __name__ == '__main__':
    main()

