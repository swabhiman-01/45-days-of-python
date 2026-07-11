#wap to find total &mpercentage mark and display student name ,gender,totalmark,
#persentage where four subject marks are given
name = input("enter the student name:")
gender = input("enter the gender:")
sub1 = float (input("enter the mark of sub1:"))
sub2 = float (input("enter the mark of sub2:"))
sub3 = float (input("enter the mark of sub3:"))
sub4 = float (input("enter the mark of sub4:"))
total = sub1+sub2+sub3+sub4
per = total * 100 / 400
print ("student nsme =",name)
print ("student gender =",gender)
print ("student totalmark =",total)
print ("student permark =",per)
              
