import numpy
from scipy.special.orthogonal import p_roots
def funkcija(f,x):
    return f(x)
def trapez(f,a,b,m):
    h = (b-a)/m
    integral = 0
    for i in range(0,m):
        integral += (f(i*h+a)*h + f(b-i*h)*h)/2
    return integral
def simpson(f,a,b,m):
    h = (b-a)/m
    integral = 0
    for i in range(0,int(m/2)):
        integral += (h*(4*f(a+h*2*i)+2*f(a+h*(2*i+1))+4*f(b-2*i*h)+2*f(b-(2*i+1)*h))/3)/2
    return integral
def fja1(x):
    return x**2
T = 300
m = 3.37*10**(-26)
kB = 1.38064852*10**(-23)
konst1 = 4*numpy.pi*((numpy.sqrt(m/(2*numpy.pi*kB*T)))**3)
konst2 = m/(2*kB*T)
def fja2(x):
    return konst1*(x**2)*numpy.exp(-konst2*(x**2))
epsilon = 0.000001
print("Trapezna metoda, 10 točaka:",round(100*trapez(fja2,509.4,609.4,10),3),"%")
print("Trapezna metoda, 50 točaka:",round(100*trapez(fja2,509.4,609.4,50),3),"%")
print("Trapezna metoda, 100 točaka:",round(100*trapez(fja2,509.4,609.4,100),3),"%")
print("Simpsonova metoda, 10 točaka:",round(100*simpson(fja2,509.4,609.4,10),3),"%")
print("Simpsonova metoda, 50 točaka:",round(100*simpson(fja2,509.4,609.4,50),3),"%")
print("Simpsonova metoda, 100 točaka:",round(100*simpson(fja2,509.4,609.4,100),3),"%")


