import jednostavnonjihalo as nj
import numpy
import matplotlib.pyplot as plt
a,b = nj.analiticki(4)
T = nj.analiticki_period()
a1,b1 = nj.euler(4,0,0,20*T,20000)
a2,b2 = nj.rk4(4,0,0,20*T,20000)
a_1,b_1 = nj.euler(4,0,0,20*T)
a_2,b_2 = nj.rk4(4,0,0,20*T)
plt.subplot(1,2,1)
plt.plot(a,b,c="r")
plt.plot(a1,b1,c="g")
plt.plot(a2,b2,c="b")
plt.legend(["Analitički","Euler","RK4"],loc="upper right")
plt.title("Usporedba za N = 20000")
plt.subplot(1,2,2)
plt.plot(a,b,c="r")
plt.plot(a_1,b_1,c="g")
plt.plot(a_2,b_2,c="b")
plt.legend(["Analitički","Euler","RK4"],loc="upper right")
plt.title("Usporedba za N = 2000")
plt.show()
