# break : used to terminate the loop when encounteres.
i = 1
while i<=5:
    print(i)
    if(i == 3):
        break
    i += 1
print("end of the loop")

# opposite of break
# continue : terminates execution in the current iteration & continues execution of the loop with the next iteration
x = 0
while x<= 5:
    if(x == 3):
        x += 1
        continue # skip
    print(x)
    x +=1
