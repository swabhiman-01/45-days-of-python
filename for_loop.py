# For loop with String
obj = "False"

for i in obj:
    print(i, end=" ")

# For loop with List
obj = [45, 67, 30, 39, 2.5, "py", 57]

for i in obj:
    print(i, end=" ")
# For loop with Tuple
obj = (10, 20, 30, 40)

for i in obj:
    print(i)
# For loop with Set
obj = {100, 200, 300, 400}

for i in obj:
    print(i)
# For loop with Dictionary
obj = {
    "Name": "Swabhiman",
    "Course": "Python",
    "Age": 19
}

for key in obj:
    print(key, ":", obj[key])
# Integer is NOT iterable
obj = 4567457

for i in obj:
    print(i)


    
