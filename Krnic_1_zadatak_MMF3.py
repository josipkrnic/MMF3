import math
from tabulate import tabulate
k = 40
suma = 1
fact = 1
suma1 = 1
clan1 = 1
suma2 = 1
fact2 = 1
suma2_konacno = 1
epsilon = 10**(-10)
lista_x = ["x","-"]
lista_k = ["k","-"]
lista_suma = ["e^-x (red)","-"]
lista_suma1 = ["e^-x (rekurzivno)","-"]
lista_suma2_konacno = ["e^-x (1/e^x)","-"]
for x in range(0,110,10):
    #razvoj u red:
    for i in range(1,k+1):
        fact = fact*i
        clan = (-x)**i/fact
        if abs(clan) > epsilon:
            suma += clan
    #rekurzivna formula:
    for j in range(1,k+1):
        clan1 = -clan1*x/j
        suma1 += clan1
    #preko e^-x = 1/e^x:
    for y in range(1,k+1):
        fact2 = fact2*y
        clan2 = x**y/fact2
        suma2 += clan2
    suma2_konacno = 1/suma2
    lista_x.append(
        x)
    lista_k.append(k)
    lista_suma.append(suma)
    lista_suma1.append(suma1)
    lista_suma2_konacno.append(suma2_konacno)
    lista_data = [lista_x,lista_k,lista_suma,lista_suma1,lista_suma2_konacno]
    suma = 1
    fact = 1
    suma1 = 1
    clan1 = 1
    suma2 = 1
    fact2 = 1
    suma2_konacno = 1
print(tabulate(lista_data))
    
