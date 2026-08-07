from functools import reduce

l = [2, 5, 67, 12, 4, 56, 6, 7, 78, 978, 90, 64, 16, 33, 23]

print(reduce(lambda n1, n2: n1 + n2, l))


print("===============using lambda function===============")


from functools import reduce

l = [2, 5, 67, 12, 4, 56, 6, 7, 78, 978, 90, 64, 16, 33, 23]

print(reduce(lambda n1, n2: n1 if n1 > n2 else n2, l))


