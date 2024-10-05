# loops are used to repeat instructions
count=1 # help of variable is Iterator
while count<=5: # For checking loop is Iteration
    print("Roopa")
    count= count +1

print(count)

i = 1
while i <= 5:
    print("Sree")
    i = i+1

# print the multiplication table of a number n
n = int(input("enter number: "))
i = 1
while i <= 10:
    print(n*i)
    i = i+1

# print the elements of the following list using loop
nums = [1, 4, 9, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx = idx +1
    
# Search specific value from given tuple
Num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 49
k = 0
while k<len(Num):
    if(Num[k]==x):
        print("Found at index", k)
        # break
    else:
        print("finding...")
    k += 1
