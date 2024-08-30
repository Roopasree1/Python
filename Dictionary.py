# dictionary is key value pair # mutable # unordered # no duplicate
dict = {
    "key" : "value",
    "name" : "roopa",
    "age" : 20,
    "is_adult" : True,
    "marks" : 83.32,
    "skills" : ["python", "java"],
    "courses" : ("cyber Security", "computer"),
    12.6 : 678
}
print(dict)
print(type(dict))
print(dict["skills"])
dict["name"] = "Roopa sree"
dict["surname"] = "Muthuluri"
print(dict)

# can also create null dictionary
# null_dict = {}
# print(null_dict)

# Nested Dictionaries
student = {
    "name" : "Nithya",
    "subjects" : {
        "phy" : 78,
        "chem" : 86,
        "math" : 88
    }
}
print(student)
print(student["subjects"])
print(student["subjects"]["math"])
print(student.keys())

# convert keys of dictionaries into list
print(list(student.keys()))

# dictionary lenght
print(len(student))
print(len(student.keys()))

# values
print(list(student.values()))

# items
print(student.items()) #tuple form
# list form 
print(list(student.items()))
# to access 1st pair in tuple through dict
pairs = list(student.items())
print(pairs[0])

# get() # returns the key according to value
print(student["name"]) # returns value
print(student.get("name")) #another method
# difference is if the value does't exits 1st method returns error but 2nd method prints none

# update()
student.update({"city":"hyderabad"})
print(student)
