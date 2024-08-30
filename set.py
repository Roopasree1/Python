# set is the collection of the unordered items
# list and dict cannot be stored in set 
# unordered # set mutable but elements in set are immutable
# set = {1,2,1,2}  # prevents duplicates # repeated elements stored only once, so it resolved to {1,2}
collection = {1, 2, 3, 4, 1, 1,"hello", "hello", "world"}
print(collection)
print(type(collection))
print(len(collection)) # ignores duplicats

# empty set syntax
name = set() # not like {} cause it can be dictionary so we use () to create empty set
print(type(collection))

#set methods
marks = {36, 78, 98}
marks.add(26)
marks.remove(36)
# we can also pass tuple but not list, dict as it is mutable and its hash can be changed
marks.add((1,2,3))
# marks.clear() removes all set
# marks.pop() random elements can be removed
print(marks)

# union set = combines both set values & returns new
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.union(set2)) #{1,2,,3,4}
# if we print original set remains same
print(set1)
print(set2)

# intersection = combines common values & returns new
set3 = {1, 2, 3}
set4 = {2, 3, 4}
print(set3.intersection(set4)) #{2,3}
