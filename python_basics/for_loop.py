#for loop
obj = [2,3,5,7,8,9]
for i in obj:
    print(i)

#sum of First natural numbers 1+2+3+4+5 = 15
#ranje(i,j) means i to j
sum = 0
for j in range(1,6):
    sum = sum + j
print(sum)

#Increment By 2
print("Increment by 2 and print")
for k in range(1,10,2):
    print(k)
print("{}{}".format("final Value of K: ",k))
