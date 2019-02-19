# from string import maketrans # for maketrans()

str = "geeksforgeeks"

str1 = "gfs"
str2 = "abc"

# using maktrans() to map elements of str2 with str1
# mapped = maketrans( str1, str2 )
# print (str.maketrans(str1, str2))
# using translate() to translate using the mapping
# print ("The string after translation using mapped elements is : ")
print  (str.translate(str.maketrans( str1, str2 ))) 
