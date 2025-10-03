# Create a tuple
person = ("Rahul", 25, 5.9)

# Print the second element (age)
print("Age:", person[1])

# Attempt to change the name
try:
    person[0] = "John"
except TypeError:
    print("Error: 'tuple' object does not support item assignment - Tuples are immutable.")
