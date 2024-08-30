# dictionary examples
dict = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture","list of facts & figures"]
    # we can store 2 values for one key in list form or tuple form 
}
print(dict)

# how many classes should have for below subjects each subject takes 1 class room
subjects = {
    "python", "java", "c++", "python", "javascript", "java",
    "python", "java", "c++", "c"
}
print(subjects)
print(len(subjects))

# give user to enter their any 3 subjects marks = use subject name as key & marks as values
marks = {} # creating empty dict for marks
# taking user input and updating the marks into marks 
x = int(input("enter phython marks: "))
marks.update({"python" : x})

x = int(input("enter java marks: "))
marks.update({"java" : x})

x = int(input("enter web development marks: "))
marks.update({"web development" : x})

print(marks)

# storing 9 and 9.0 
values= {
    ("float", 0.9),
    ("int", 9)
}
print(values)