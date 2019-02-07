
#Initial Template for Python 3
def check_status(a, b, status):
    ##Your code here
    ##Either True or False is returned
    if(status == True):
      if(a<0 and b<0):
        return True
      else:
        return False
    elif(a>0 and b>0):
      return False
    elif(a>0 or b>0):
      return True
    else:
      return False
# Driver Code
def main():
    
    # Testcase input
    testcases = int(input())
    
    # Looping through testcases
    while(testcases > 0):
        a = int(input())
        b = int(input())
        flag = input()
        
        if(flag == "True"):
            flag = True
        else:
            flag = False
        
        if(check_status(a, b, flag) is True):
            print ("True")
        else:
            print ("False")
        
        testcases -= 1
 
if __name__ == '__main__':
    main()


