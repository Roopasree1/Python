# practice print elements of the following list using loop
List = [1,4,9,16,7,89,78,0,5]
for val in List:
    print(val)

# serach for a number x in this tuple using loop
num = (1,4,6,7,8,9,2)
x = 4
idx = 0 
for i in num:
    if(i == x):
        print("element is found at index", idx)
    idx += 1

# WAP to find the sum of first n numbers. (using while)
n = 5
sum = 0
for c in range(1, n+1):
    sum = sum + c
print("total sum=",sum)

# Factorial
n = 5
fact = 1
i = 1
while i <= n:
    fact = fact * i
    i += 1
print("factorial =", fact)

# also using range function
# n = 5
# fact = 1
# for i in range(1, n+1):
#    fact *= i
# print("factorial =", fact)



