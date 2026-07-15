l=[20,0,10,20,-20,67]
print("given list = ", l)
l.append(35)
print("after append list = ", l)
l.insert(3,89)
print("after insert list =", l)
print(l.pop())
print("after pop list = ", l)
print(l.pop(1))
print("after pop list = ", l)
l.remove(-20)
print("after remove list = ",l)
l1=[20,67,88]
l.extend(l1)
print("after extend list = ",l)
print("count element 20 =" ,l.count(20))
print("count element 200 =", l.count(200))
print("list =",l)
l.reverse()
print("after reverse list = ",l)
l.sort(reverse = True)
print("after Desc sort list=",l)
l1 = [10,20,30]
l2 = [10,20,30]
print(l1 == l2)
l3 = l1.copy()
print("l3=",l3)
l3.clear()
print("l3=",l3)


