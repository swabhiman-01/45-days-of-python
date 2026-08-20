import matplotlib.pyplot as plt
Day = ['1st','2nd','3rd','4th','5th','6th','7th']
Temp = [38.49,40.36,40.98,39.56,41.01,40.78,41.99]
plt.plot(Day,Temp,marker = "o",markersize= 10,mec = "blue",mfc = "red", color = "red")
plt.title("1st 7 days jun month temp graph in (c)")
plt.xlabel("Days")
plt.ylabel("Temp in c")
plt.grid(axis = "y",color = "green")
plt.show()
