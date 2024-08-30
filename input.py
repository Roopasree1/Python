# input() = taking input from user & printing
'''
name = input("name: ")
print(name)
age = int(input("age: "))
print(age)
price = float(input("price: "))
print(price)
# print("My name is",name,"and my age is",age)'''

# example traffic
light=input("light: ")
if(light=="red"):
    print("stop")
elif(light=="yellow"):
    print("look")
elif(light=="green"):
    print("go")
else:
    print("light is broken")

# operations (logical operator)
val1 = True
val2 = False
print("And operator:", val1 and val2)
print("Or operator:", val1 or val2)

#Type Conversion (automatic convertion)
x = 2
y = 4.67
sum = x+y
print(sum)

#type casting 
p = int("2")
q = 4.24
print(type(p))
print(p+q)

#example 
#for string
name1 = input("enter your name1red: ")
print("welcome", name1)
#for int output = type casting should be done
age1 = int(input("enter your age: "))
print(type(age1), age1)

# area of the square
side = float(input("enter square side: "))
print("area:", side * side)