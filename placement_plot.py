import matplotlib.pyplot as plt
comp_name = ["TCS","HCL","DEL","WIP","CS","IBM","GOOGLE","MICROSOFT","PWC","ASC","NOT PLACED"]
num_students = [56,78,45,32,76,89,34,88,93,46,135]
colors = ["green","red","pink","black","orange","blue","yellow","#ababab","#ab1245","#ffab12","#9cab12"]
'''
plt.bar (comp_name,num_students,width = 0.7,color = colors)

plt.xlabel("comp name")
plt.ylabel("number of students")
plt.grid(axis= "y")
'''
plt.barh (comp_name,num_students,height= 0.7,color = colors)

plt.ylabel("comp name")
plt.xlabel("number of students")

plt.show()
















