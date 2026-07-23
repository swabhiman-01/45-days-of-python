s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}

print(s1)
print(s2)

print(s1.union(s2))

s3 = s1.copy()
s3.update(s2)
print(s3)

print(s1.difference(s2))

s4 = s1.copy()
s4.difference_update(s2)
print(s4)

print(s1.intersection(s2))

s5 = s1.copy()
s5.intersection_update(s2)
print(s5)

print(s1.symmetric_difference(s2))

s6 = s1.copy()
s6.symmetric_difference_update(s2)
print(s6)

s7 = s1.copy()
s7.add(70)
print(s7)


s8 = s1.copy()
print(s8)


s9 = s1.copy()
s9.remove(20)
print(s9)

print(s1)
s1.discard(30)
print(s1)

s1 = {10, 20, 30, 40}
s2 = {30,20}
s3 = {3,6,2}
print(s1.issubset(s2))
print(s2.issubset(s1))
print(s1.issuperset(s2))
print(s2.issuperset(s1))
























