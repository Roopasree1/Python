# functipons: block of statements that perform a specific task
# we can call the function as many times we want
def sum(a,b):  # function definition # parameters
    c=a+b
    print(c)
    return c

sum(2,4)       # function call; # aeguments
# calling 2nd time
sum(3,6)

# or
def cal_sum(x,y):
    return x+y

sum = cal_sum(1,7) 
print(sum)

#example
def hello():
    print("Hello")

hello()
hello()

# average of 3 marks
def average(e, f, g):
    total = e+f+g
    avg = total / 3
    print(avg)
    return avg
average(34,67,89)

# prime
def prime(n):
    if n % 2 == 0:
        print("prime")
    else:
        print("not prime")
prime(2)

# sep = " "  sep is automatically define space in print function or other
print("Roopa","Jana")

# end = " " end means it takes next line to frst line prints one beside another by giving space
print("kavya", end=" ") # multiple lines into same line end is used
print("Nithya") # end = "\n" # end= "$" any thing can be passed betwwen 

# pre- defined functions
# print(), len(), type(), range() ect

# user define functions 
# programs writes pre- defined functions

# default parameters
# assigning a deafault value to parameter, which is used when no argument is passes
#def multi(k, l):
#    print(k*l)
#    return k*l
#multi() # error
# so we have give some default values in function define
def mult(m=3, n=9):
    print(m*n)
    return m*n
mult() 
# we can also make single value default but only for frst parameter








