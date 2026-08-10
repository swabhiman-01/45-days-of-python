def Add(*args):
    print("Type of args =", type(args))
    print("All arguments =", args)
    print("Sum of all arguments =", sum(args))

print(Add(56, 65))

print(Add(56, 65, 98, 66, 72, 32))


