# tuple is immutable
tuple = (2, 3, 4, 2)
print(type(tuple))
print(tuple[0])
# tuple[0] = 7 is not possible cause it is immutable
# string and tuple are immutable 
# tuple= (1,)
# print(type(tuple)) if we dont keep , then it python takes as int
print(tuple[1:3])
print(tuple.index(2)) # 1st occurance
print(tuple.count(2)) # counts total occurences

# num of same A grades from all grades
grade = ("C", "A", "D", "A", "A")
print(grade.count("A"))

# store ascending to decending
numbers = []
