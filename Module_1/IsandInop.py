
#Initial Template for Python 3
def number_present(num, query):
    #num is a 'list', query is a 'int'
    for i in range(len(num)):  
                             
        if (num[i] is query) :
                             
            return True
    return False 
def main():
    testcases = int(input())
    while testcases :
        num = input()
        num = num.split()
        for i in range(len(num)):
            num[i] = int(num[i])
        
        q = input()
        q = q.split()
        for i in range(len(q)):
            q[i] = int(q[i])
            
        for i in range(len(q)):
            if number_present(num, q[i]):
                print("True")
            else:
                print("False")
        testcases-=1
if __name__ == '__main__' :
    main()


