#python has three main datatypes
#1.Numeric ( Int, Float, Complex)
#2.String
#3. List

a,b,c=1, 2.3,"Upulika"

d= "Not like in other languages in Python when concatenating  two different variable types it should use format method"
print(d)


print(a)
print("{}{}".format("Type of a is ",type(a)))
print(b)
print("{}{}".format("Type of b is ",type(b)))
print(c)
print("{}{}".format("Type of c is ",type(c)))

print("In Python List data type we can add different data type values in to the same list")

values = [1, "Upulika", 2.5]
print(values)
print(values[0])
print(values[1])
print(values[2])
print(values[-1])
print("To insert values we are using insert method")
values.insert(2,"Katupitiya")
print(values)
print("<append> add values to end")
values.append("End")
print(values)
print( "if we want to update value we can give it using index no and also can delete values")

values[3]=100
print(values)
del values[3]
print(values)


