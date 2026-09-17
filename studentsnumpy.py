import numpy as np
students = np.array(['DEVA','BAPU','RAJ','SUBHU','NAMI','LIMA','SONY','KRIS'])
marks = np.array([
    [10,20,30,40,50],
    [87,80,66,83,90],
    [20,10,30,50,80],
    [10,40,70,80,90],
    [20,30,40,50,60],
    [40,50,60,70,90],
    [20,50,70,90,78],
    [30,50,60,70,80]
    ])
subjects = np.array(["Odia","Python","Math","DBMS","Eng"])
print(students.shape)
print(marks.shape)
print(students.ndim)
print(marks.ndim)

total = np.sum(marks,axis=1)
print(total)

for i in  range (len(students)):
    print(students[i],'=',total[i])

per= total/5
for i in range(len(students)):
    print(students[i],"->",total[i],"->",per[i],"%")


topper_index = np.argmax(total)
print("Topper student Name =", students[topper_index])
print("Total marks",total[topper_index])
print("per marks",per[topper_index])

lowest_index = np.argmin(total)
print("lowest student Name =", students[lowest_index])
print("Total marks",total[lowest_index])
print("per marks",per[lowest_index])

subject_avg = np.mean(marks,axis = 0)
for i in range(len(subjects)):
    print(subjects[i],"->",'Avarage Marks =',subject_avg[i])

diff_index = np.argmin(subject_avg)
print("lowest avarage subject =",subjects[diff_index])
print("lowest avarage subject marks =",subject_avg[diff_index])

best_index = np.argmax(subject_avg)
print("Highest avarage subject =",subjects[best_index])
print("Highest avarage subject marks =",subject_avg[best_index])

result1 = per >= 80
print(result1)


result2 = per <50
print(result2)

pass_data = np.all(marks >= 40,axis = 1)
print(students[pass_data])





























































