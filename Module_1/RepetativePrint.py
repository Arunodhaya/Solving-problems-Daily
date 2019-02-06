def print_fun(string, x):
    return print(string * x, sep=" ")
# Driver Code
def main():
    testcases = int(input())
    
    # Loop for testcases
    while(testcases > 0):
        string = input()
        x = int(input())
        print_fun(string, x)
        testcases -= 1
if __name__ == '__main__':
    main()
    