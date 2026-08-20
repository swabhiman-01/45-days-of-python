import matplotlib.pyplot as plt
year = [1950,1960,1970,1980,1990,2000,2010,2026]
ind_pop = [3.245,5.45,8.456,11.245,14.22,16.784,18.93,22.154]
chi_pop = [3.976,6.78,8.954,12.88,15.78,17.90,19.324,21.547]
plt.plot(year,ind_pop,color = "orange",linewidth=3,marker = "*",mfc = "blue",mec = "blue",markersize = 15)
plt.plot(year,chi_pop,color = "red",linewidth= 2 ,marker = "o",mfc = "red",mec = "green",markersize = 13)
plt.xlabel("year in each 10",color = 'green')
plt.xlabel("population in bill",color = 'red')
plt.grid(axis='x',color = 'yellow',linewidth=0.5)
plt.legend(["india","china"])

plt.title("india vs china population",color = "blue")
plt.show()
