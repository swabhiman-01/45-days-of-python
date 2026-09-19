import pandas as pd

data = {"Name":['Amit','Raj','Lima','Alok','Deva','Bapu'],
        'Age':[19,22,25,28,21,18],
        "Gender":['M','M','FE','M','M','M'],
        "Dept":["CSE","CST","ME","EE","ME","CST"]
        }

obj = pd.DataFrame(data)
print(obj)
print(obj.head(3) )
print(obj.tail())
print(obj.info())
print(obj.iloc() )
print("==============================================================")

obj  ["Total_mark"]=[546,786,654,390,701,608]
obj  ["Cast"]=["SC","OBC","GENERAL","OBC","ST","GENERAL"]
print(obj)

obj.drop('Dept',axis = 1 ,inplace = True)
print(obj)

obj.drop(3,axis = 0 ,inplace = True)
print(obj)

obj.rename(columns = {"Name":"StudentName","Dept":"DeptName"}, inplace = True)

obj2 = obj.to_csv('studentdata.csv',index = True)













