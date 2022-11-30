import numpy
import Lagrange
import matplotlib.pyplot as plt
import scipy.interpolate as si
import polint
r = []
V = []
datoteka = open("V(H-H).txt", "r")
n = 1
for linija in datoteka:
    if n > 2:
        podaci = [float(x) for x in linija.split()]
        r.append(0.52917721092*podaci[0])
        V.append(315775.04*podaci[1])
    n = n + 1
datoteka.close()
datoteka2  = open("V(H-H)_AK.txt","w")
for i in range(len(r)):
    datoteka2.writelines("{}\t{}\n".format(r[i],V[i]))
datoteka2.close()
datoteka3 = open("V(H-H)_inter.txt","w")
x = numpy.linspace(2.81,9.82,num=71)
y_L = []
y_P = []
splajn = si.CubicSpline(r,V)
y_S = splajn(x)
for i in range(len(x)):
    yi = Lagrange.Lagrange(r,V,len(r),x[i])
    yip, dyp = polint.polint(r,V,len(r),x[i])
    y_L.append(yi)
    y_P.append(yip)
    datoteka3.writelines("x = {}, {}, {}, {}, {}, {}\n".format(i,yi,yip,dyp,y_S[i],yip - y_S[i]))
datoteka3.close()
plt.xlim(0,10.5)
plt.ylim(-10,10)
plt.plot(x,y_L,c="g",label = "Lagrange")
plt.plot(x,y_P,"x",c="r",label ="Neville")
plt.scatter(r,V,c="orange", label = "r_i,V_i")
plt.scatter(x,y_S,c ="b",label="Splajn")
plt.legend()
plt.show()
                         
