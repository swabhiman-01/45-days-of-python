obj = [10, 20, -10, 34, 45, -7, 0]

print("List elements:", obj)
print("Number of elements:", len(obj))
print("Maximum element:", max(obj))
print("Minimum element:", min(obj))
print("Sum of elements:", sum(obj))

print("List in Ascending Order:", sorted(obj))
print("List in Descending Order:", sorted(obj, reverse=True))

print(obj)
del(obj)
print(obj)
