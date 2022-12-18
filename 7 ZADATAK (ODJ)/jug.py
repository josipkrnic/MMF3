import numpy
import matplotlib.pyplot as plt
import jednostavnonjihalo as nj
def jug(theta0,w0,t0=0,tN=20,N=20000,g=9.81,m=0.2,l=0.2484902028828339):
    t = [t0]
    w = [w0]
    alfa = [-g/l*numpy.sin(theta0*numpy.pi/180)]
    theta = [theta0*numpy.pi/180]
    h=(tN-t0)/N
    for i in range(1,N):
        t.append(i*h)
        w.append(w[i-1]+alfa[i-1]*h)
        theta.append(theta[i-1]+w[i-1]*h+alfa[i-1]*h**2/2)
        alfa.append(-g/l*numpy.sin(theta[i]))
    return t,theta,w,alfa
a,b,c,d = jug(4,0)
plt.plot(b[17000:19999],c[17000:19999],c="b")
f,g,h,j = nj.euler(4,0,0,20,20000)
f1,g1,h1,j1 = nj.rk4(4,0,0,20,20000)
plt.plot(g[17000:19999],h[17000:19999],c="g")
plt.plot(g1[17000:19999],h1[17000:19999],c="r")
plt.legend(["JUG","EULER","RK4"])
plt.show()
