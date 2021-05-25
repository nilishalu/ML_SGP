import numpy as np
import matplotlib.pyplot as plt

def estimate_coeff(x,y):
    n=np.size(x)

    m_x=np.mean(x)
    m_y=np.mean(y)

    S_xx=np.sum(x*x)-n*m_x*m_x
    S_xy=np.sum(x*y)-n*m_x*m_y

    b_1=S_xy/S_xx
    b_0=m_y-b_1*m_x

    return (b_0,b_1)

def plot_regression_line(x,y,b):

    plt.scatter(x,y,color = "black",marker="s",s = 30)

    y_pred=b[0]+b[1]*x

    plt.plot(x,y_pred,color ="blue")

    plt.xlabel('No. of hours studied')
    plt.ylabel('Percentage scored')

    plt.show()

def main():

    x=np.array([1,3,2,5,7,8,8,9,10,12])
    y=np.array([0,10,20,30,40,50,60,70,80,90])

    b=estimate_coeff(x,y)

    print("Estimated Coefficients:\nb_0={} \nb_1={}".format(b[0],b[1]))

    plot_regression_line(x,y,b)

if __name__ == "__main__":
    main()