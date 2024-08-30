# list is mutable
# marks1 = 25
# marks2 = 56
# instead
marks = [98.6, 87, 94, 65, 75]
print(marks)
print(type(marks))
print(marks[2])
print(marks[0])
print(len(marks))

# multiple types of data we can store in a single list
student = ["Roopa", 20, 83.32, "Hyderabad"]
print(student)
student[0] = "Sree"
print(student)
#In python string is immutable and lists is mutable

Branch = ["csc", "csm", "csd", "cse"]
print(Branch[1:3]) #if starting or ending is not given in slice all values will come

# question for list
movies = []
movie1 = input("enter your first fav movie: ")
movie2 = input("enter your second fav movie: ")
movie3 = input("enter your third fav movie: ")
movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print(movies)

# palindrome
list = [1,2,3,2,1]
copy_list = list.copy()
copy_list.reverse()

if(copy_list == list):
    print("Palindrome")
else:
    print("Not Palindrome")

# store ascending to decending using list
numbers = [2,5,4,6,3,1]
numbers.sort()
print(numbers)





