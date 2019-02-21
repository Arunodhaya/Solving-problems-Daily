import re
def Imgextractor(str):
#     pat= re.compile(r'^www\.[a-z]|[A-Z]|\W|\d./jpg$') 
      pat = re.findall(r'<img\s+[^>]*?src=("|\')([^"\']+)\1',str)
#       match=pat.finditer(str)
      return pat
   
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        mystr=input()
        print(Imgextractor(mystr))
        testcases-=1
        
if __name__=='__main__':
    main()
