import numpy as np
import matplotlib.pyplot as plt

#levels of the jobs
X=[1,2,3,4,5,6,7,8,9,10]
#salary  distribution based on levels
Y=[45000,50000,60000,80000,110000,150000,200000,300000,500000,1000000]

degree=4
#degree 4 suited more to the relationship so that to minimise the errors.
# It is the smallest degree with minimized error better than 2 and 3
poly_fit =np.poly1d(np.polyfit(X,Y,degree))

xx = np.linspace(0,26,100)
plt.plot(xx,poly_fit(xx),c='r',linestyle='-')
plt.title('Salary data')
plt.xlabel('Level of job ')
plt.ylabel('Salary')
plt.axis([0,12,0,1050000])
plt.grid(True)
plt.scatter(X,Y)
plt.show()
