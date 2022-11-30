import numpy
T = 300
masa = 3.37*10**(-26)
kB = 1.38064852*10**(-23)
konst1 = 4*numpy.pi*((numpy.sqrt(masa/(2*numpy.pi*kB*T)))**3)
konst2 = masa/(2*kB*T)
def funkcija(f,x):
    return f(x)
def fja(x):
    return konst1*(x**2)*numpy.exp(-konst2*(x**2))
x1 = 509.4
x2 = 609.4
epsilon = 0.00001
n = 101
m = int((n+1)/2)
xm = 0.5*(x2+x1)
xl = 0.5*(x2-x1)
zlista = []
def Legendarni_polinom(n,x):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        Lp = [1,x]
        for i in range(1,n):
            Lp.append(((2*i+1)*x*Lp[i]-i*Lp[i-1])/(i+1))
        Lp.reverse()
        Lp_n = Lp[0]
        return Lp_n
def derivacija_Legendarnog_polinoma(n,x):
    dLp = n*(x*Legendarni_polinom(n,x)-Legendarni_polinom(n-1,x))/(x**2-1)
    return dLp
if n%2 == 0:
    for i in range(1,m+1):
        z = numpy.cos(numpy.pi*(i-0.25)/(n+0.5))
        granica = 1
        k = 0
        while(granica>epsilon):
            z = z - Legendarni_polinom(n,z)/derivacija_Legendarnog_polinoma(n,z)
            k += 1
            granica = abs(Legendarni_polinom(n,z)/derivacija_Legendarnog_polinoma(n,z))
        zlista.append(z)
    z_neg = []
    for g in zlista:
        z_neg.append(-g)
    zlista.reverse()
    nultocke = []
    if n%2 == 0:
        nultocke = z_neg + zlista
    else:
        nultocke = z_neg
        nultocke.append(0)
        nultocke += zlista
    iks = []
    w = []
    for s in nultocke:
        iks.append(xm - xl*s)
        w.append(2/((1-s**2)*(derivacija_Legendarnog_polinoma(n,s)**2)))
    rješenje = 0
    def funk(x):
        return x**2
    for r in range(0,len(w)):
        rješenje += (x2-x1)*(fja(iks[r])*w[r])/2
    print(rješenje)
else:
    for i in range(1,m):
        z = numpy.cos(numpy.pi*(i-0.25)/(n+0.5))
        granica = 1
        k = 0
        while(granica>epsilon):
            z = z - Legendarni_polinom(n,z)/derivacija_Legendarnog_polinoma(n,z)
            k += 1
            granica = abs(Legendarni_polinom(n,z)/derivacija_Legendarnog_polinoma(n,z))
        zlista.append(z)
    z_neg = []
    for g in zlista:
        z_neg.append(-g)
    zlista.reverse()
    nultocke = []
    if n%2 == 0:
        nultocke = z_neg + zlista
    else:
        nultocke = z_neg
        nultocke.append(0)
        nultocke += zlista
    iks = []
    w = []
    for s in nultocke:
        iks.append(xm - xl*s)
        w.append(2/((1-s**2)*(derivacija_Legendarnog_polinoma(n,s)**2)))
    rješenje = 0
    def funk(x):
        return x**2
    for r in range(0,len(w)):
        rješenje += (x2-x1)*(fja(iks[r])*w[r])/2
    print(rješenje)

    

        
    
    
        
        
        
        
        
        

        


