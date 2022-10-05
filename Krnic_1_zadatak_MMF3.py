import math
from tabulate import tabulate
import numpy as np
k = 180
suma = 1
fact = 1
suma1 = 1
clan1 = 1
suma2 = 1
fact2 = 1
suma2_konacno = 1
broj_clanova = 0
cl = 0
cl1 = 0
cl2 = 0
e_na_x = 0
obr_e_na_x = 0
epsilon = 10**(-10)
lista_x = ["x","-"]
lista_k1 = ["k1","-"]
lista_k2 = ["k2","-"]
lista_suma = ["e^-x (red)","-"]
lista_suma1 = ["e^-x (rekurzivno)","-"]
lista_suma2_konacno = ["e^-x (1/e^x)","-"]
lista_xje20 = []
lista_tocno = ["tocno","-"]
lista_xje20_2 = []
lista_k3 = ["k3", "-"]
lista_xje20_3 = []
for x in range(0,110,10):
    #razvoj u red:
    for i in range(1,k+1):
        fact = fact*i
        clan = (-x)**i/fact
        if abs(clan) > epsilon:
            suma += clan
            cl += 1
            if x == 20:
                lista_xje20.append(clan)
    #rekurzivna formula:
    for j in range(1,k+1):
        clan1 = -clan1*x/j
        if abs(clan1) > epsilon:
            suma1 += clan1
            cl1 += 1
            if x == 20:
                lista_xje20_2.append(clan1)
    #preko e^-x = 1/e^x:
    for z in range(1,k+1):
        fact2 = fact2*z
        clan2 = x**z/fact2
        if clan2 > epsilon:
            suma2 += clan2
            cl2 += 1
            if x == 20:
                lista_xje20.append(clan2)
    e_na_x = np.exp(x)
    obr_e_na_x = 1/(e_na_x)
    suma2_konacno = 1/suma2
    lista_k1.append(cl)
    lista_k2.append(cl1)
    lista_k3.append(cl2)
    lista_x.append(x)
    lista_suma.append(suma)
    lista_suma1.append(suma1)
    lista_suma2_konacno.append(suma2_konacno)
    lista_tocno.append(obr_e_na_x)
    lista_data = [lista_x,lista_k1,lista_k2,lista_k3,lista_suma,lista_suma1,lista_suma2_konacno,lista_tocno]
    suma = 1
    fact = 1
    suma1 = 1
    clan1 = 1
    suma2 = 1
    fact2 = 1
    suma2_konacno = 1
    cl = 0
    cl1 = 0
    cl2 = 0
    e_na_x = 0
    obr_e_na_x = 0
print(tabulate(lista_data))
print("Za x = 20 (red) svi članovi su: ",lista_xje20)
print("Za x = 20 (rekurzivna) svi članovi su: ",lista_xje20_2)
print("Za x = 20 (1/e^x) +svi članovi su: ",lista_xje20_3)
    
