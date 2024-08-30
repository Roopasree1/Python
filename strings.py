# strings1
str1 = "this is string.\nwe are creating in python."
print(str1)

# string concatenation
str2 = "Roopa"
str3 = "Sree"
str4 = str2+str3
print(str4)
print(len(str2)) # if there is space between string it is counted as length

#indexing
str5 = "Roopa_sree"
print(str5[5])

# slicing (imp in machine learning)
# str[starting_idx : ending_idx] ending idx is not included
str6 = "ApnaCollege"
print(str6[1:6])
# Negetive index in slicing backonwards and starts from -1
str7 = "Apple"
print(str7[-3:-1]) #same ending index doesnt count

# odd or even
value = int(input("enter the number:"))
if(value % 2==0):
    print("even")
else:
    print("odd")

#greatest of 3 numbers
l = int(input("enter the first number:"))
m = int(input("enter the second number:"))
n = int(input("enter the third number:"))

if(l>=m and l>=n):
    print("the first number is larger:", l)
elif(m>n):
    print("the second number is larger:", m)
else:
    print("the third number is larger:", n)
