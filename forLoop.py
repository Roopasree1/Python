# loops are used for sequential traversal. For traversing list, string, tuples etc
# for Loops             
# for el in list:
# some work
list = [1,2,3,4,5]
for el in list:
    print(el)

names = ["divya", "Roopa", "gayatri", "pragnya"]
for val in names:
    print(val)

str = "Roopa"
for ob in str:
    print(ob)

# else is optional to print after the for loop
str1 = "jana"
for i in str1:
    print(i)
else: # else is used when break used
    print("thats it")

str3 = "apnacollege"
for char in str3:
    if(char == 'o'):
        print("o found")
        break
    print(char)
print("end")

# range function : range function returns a sequence of numbers, starting from 0 by default, and increments by 1(by default), and stops before a specified number.
# range (start?, stop, step?)
seq = range(10)
for f in seq:
    print(f) 
# or
# for f in range(10): # range(stop)
#      print(i)

# for f in range(2,10): # range(start,stop) stop dost include
#      print(i)

# for f in range(2,10,2): # range(start, stop, stop)
#      print(i)

# printing even and odd numbers using range function
for k in range(2, 101, 2):
    print(k)
# odd
for j in range(1, 100, 2):
    print(j)

# print multiplication table of a number n
n = int(input("enter the number: "))
for c in range(1, 11):
    print(n * c)

# pass statement : pass is a null statement that does nothing. it is used as a placeholder for future code
# for el in range(10):
#      pass
for el in range(5):
    pass
print("when no work done for for loop or other than pass is used")




