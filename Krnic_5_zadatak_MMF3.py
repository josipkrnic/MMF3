import numpy
import matplotlib.pyplot as plt
def funkcija(f,x,y01,y02,A,B,C,D):
    return f(x,y01,y02,A,B,C,D)
def bisekcija(f,a,b,epsilon):
    if numpy.sign(f(a)) == numpy.sign(f(b)):
        print("Početni uvjet nije zadovoljen.")
    c = (a+b)/2
    if abs(f(c)) < epsilon:
        return c
    if numpy.sign(f(a)) == numpy.sign(f(c)):
        return bisekcija(f,c,b,epsilon)
    elif numpy.sign(f(b)) == numpy.sign(f(c)):
        return bisekcija(f,a,c,epsilon)
#definiramo funkciju u kojoj možemo izmjenjivati parametre A,B,C,D i početne položaje, a u zadatku koristimo podatke s teamsa
def f(x,y01=5,y02=0.325,A=1,B=3,C=2,D=0.5):
    return y01 + A*numpy.cos(B*x) - y02- C*numpy.exp(D*x)
#prva dva pribrojnika čine funkciju y1(t), a druga 2 y2(t) i nultočka koju računamo je za razliku tih funkcija
#gornja funkcija daje nam y(t) na kojem će se tijela nalaziti u trenutku sudara
#mogli smo uzeti bilo koju od dvije f-je, uzimamo prvu
def f1(x,y01=5,y02=0,A=1,B=3,C=0,D=0):
    return y01 + A*numpy.cos(B*x) - y02 - C*D
x0 = bisekcija(f,2,4,0.001)
y0 = f(x0)
y0_t = f1(x0)
print("Nul-točka u zadanom intervalu je: (",x0,",",y0,")")
print("Točka sudara je: (",x0,",",y0_t,")")
#definiramo derivaciju razlike funkcija
def df(x,y01=5,y02=0.325,A=1,B=3,C=2,D=0.5):
    return -A*B*numpy.sin(B*x) - D*C*numpy.exp(D*x)
#Newton-Raphson
x0_2 = 2
epsilon_NR = 0.0001
while abs(f(x0_2)/x0_2)>=epsilon_NR:
    x0_2 = (x0_2 - f(x0_2)/df(x0_2))
print("Nul-točka dobijena Newton-Raphsonovom metodom je x0 =",x0_2)
x = numpy.linspace(-5,5,10000)
y1 = 5 + numpy.cos(3*x)
y2 = 0.325 + 2*numpy.exp(0.5*x)
plt.plot(x,y1)
plt.plot(x,y2)
plt.show()
    
                    
