import numpy
from tabulate import tabulate
import matplotlib.pyplot as plt
#1 DIO ZADATKA:
def funkcija(f, x):
    return f(x)
def derivacija(f, x, h):
    derivacija_unaprijed = (f(x+h) - f(x))/h
    derivacija_unazad = (f(x) - f(x-h))/h
    centralna_derivacija = (f(x+h)- f(x-h))/(2*h)
    return derivacija_unaprijed, derivacija_unazad, centralna_derivacija
def der5(f, x, h):
    deriv5 = (-f(x+2*h)+8*f(x+h)-8*f(x-h)+f(x-2*h))/(12*h)
    return deriv5
def f(x):
    return numpy.exp(x)
lista_h = ["tip","der. unaprijed (df_2)","der. unatrag","der. centralna (df3)","derivacija_5"]
lista_derivacija = []
lista_derivacija1 = ["x=0.5,h=10^-6"]
for i in range(0,3):
    df1_1 = derivacija(f, x = 0.5, h = 0.000001)[i]
    lista_derivacija1.append(df1_1)
lista_derivacija1.append(der5(f,x=0.5,h=0.000001))
lista_derivacija2 = ["x=0.5,h=10^-4"]
for i in range(0,3):
    df1_2 = derivacija(f, x = 0.5, h = 0.0001)[i]
    lista_derivacija2.append(df1_2)
lista_derivacija2.append(der5(f,x=0.5,h=0.0001))
lista_derivacija3 = ["x=0.5,h=10^-1"]
for i in range(0,3):
    df1_3 = derivacija(f, x = 0.5, h = 0.1)[i]
    lista_derivacija3.append(df1_3)
lista_derivacija3.append(der5(f,x=0.5,h=0.1))
lista_derivacija4 = ["x=1.5,h=10^-6"]
for i in range(0,3):
    df2_1 = derivacija(f, x = 1.5, h = 0.000001)[i]
    lista_derivacija4.append(df2_1)
lista_derivacija4.append(der5(f,x=1.5,h=0.000001))
lista_derivacija5 = ["x=1.5,h=10^-4"]
for i in range(0,3):
    df2_2 = derivacija(f, x = 1.5, h = 0.0001)[i]
    lista_derivacija5.append(df2_2)
lista_derivacija5.append(der5(f,x=1.5,h=0.0001))
lista_derivacija6 = ["x=1.5,h=10^-1"]
for i in range(0,3):
    df2_3 = derivacija(f, x = 1.5, h = 0.1)[i]
    lista_derivacija6.append(df2_3)
lista_derivacija6.append(der5(f,x=1.5,h=0.1))
lista_derivacija7 = ["x=2.5,h=10^-6"]
for i in range(0,3):
    df3_1 = derivacija(f, x = 2.5, h = 0.000001)[i]
    lista_derivacija7.append(df3_1)
lista_derivacija7.append(der5(f,x=1.5,h=0.000001))
lista_derivacija8 = ["x=2.5,h=10^-4"]
for i in range(0,3):
    df3_2 = derivacija(f, x = 2.5, h = 0.0001)[i]
    lista_derivacija8.append(df3_2)
lista_derivacija8.append(der5(f,x=2.5,h=0.0001))
lista_derivacija9 = ["x=2.5,h=10^-1"]
for i in range(0,3):
    df3_3 = derivacija(f, x = 2.5, h = 0.1)[i]
    lista_derivacija9.append(df3_3)
lista_derivacija9.append(der5(f,x=2.5,h=0.1))
lista_derivacija = [lista_h,lista_derivacija1,lista_derivacija2,lista_derivacija3,lista_derivacija4,lista_derivacija5,lista_derivacija6,lista_derivacija7,lista_derivacija8,lista_derivacija9]
print(tabulate(lista_derivacija))
#2 DIO ZADATKA
def druga_derivacija(f,x,h):
    dr_der = (f(x+h)-2*f(x)+f(x-h))/(h*h)
    return dr_der
lista_h_vrijednosti =["x","10^-6","10^-5","10^-4","10^-3","10^-2","10^-1"]
lista_h_brojevi = [0.000001, 0.00001,0.0001,0.001,0.01,0.1]
lista_x_je_1 = ["1"]
lista_x_je_2 = ["2"]
lista_x_je_3 = ["3"]
lista_x_je_4 = ["4"]
lista_x_je_5 = ["5"]
lista_x_je_6 = ["6"]
lista_x_je_7 = ["7"]
lista_x_je_8 = ["8"]
lista_x_je_9 = ["9"]
lista_x_je_10 = ["10"]
greska_1 = ["greška"]
greska_2 = ["greška"]
greska_3 = ["greška"]
greska_4 = ["greška"]
greska_5 = ["greška"]
greska_6 = ["greška"]
greska_7 = ["greška"]
greska_8 = ["greška"]
greska_9 = ["greška"]
greska_10 = ["greška"]
h_lista = [0.000001,0.00001,0.0001,0.001,0.01,0.1]
for i in h_lista:
    d2f_1 = druga_derivacija(f,x=1,h=i)
    error1 = abs((d2f_1-numpy.exp(1))/(numpy.exp(1)))
    lista_x_je_1.append(d2f_1)
    greska_1.append(error1)
for i in h_lista:
    d2f_2 = druga_derivacija(f,x=2,h=i)
    error2 = abs((d2f_2-numpy.exp(2))/(numpy.exp(2)))
    lista_x_je_2.append(d2f_2)
    greska_2.append(error2)
for i in h_lista:
    d2f_3 = druga_derivacija(f,x=3,h=i)
    error3 = abs((d2f_3-numpy.exp(3))/(numpy.exp(3)))
    lista_x_je_3.append(d2f_3)
    greska_3.append(error3)
for i in h_lista:
    d2f_4 = druga_derivacija(f,x=4,h=i)
    error4 = abs((d2f_4-numpy.exp(4))/(numpy.exp(4)))
    lista_x_je_4.append(d2f_4)
    greska_4.append(error4)
for i in h_lista:
    d2f_5 = druga_derivacija(f,x=5,h=i)
    error5 = abs((d2f_5-numpy.exp(5))/(numpy.exp(5)))
    lista_x_je_5.append(d2f_5)
    greska_5.append(error5)
for i in h_lista:
    d2f_6 = druga_derivacija(f,x=6,h=i)
    error6 = abs((d2f_6-numpy.exp(6))/(numpy.exp(6)))
    lista_x_je_6.append(d2f_6)
    greska_6.append(error6)
for i in h_lista:
    d2f_7 = druga_derivacija(f,x=7,h=i)
    error7 = abs((d2f_7-numpy.exp(7))/(numpy.exp(7)))
    lista_x_je_7.append(d2f_7)
    greska_7.append(error7)
for i in h_lista:
    d2f_8 = druga_derivacija(f,x=8,h=i)
    error8 = abs((d2f_8-numpy.exp(8))/(numpy.exp(8)))
    lista_x_je_8.append(d2f_8)
    greska_8.append(error8)
for i in h_lista:
    d2f_9 = druga_derivacija(f,x=9,h=i)
    error9 = abs((d2f_9-numpy.exp(9))/(numpy.exp(9)))
    lista_x_je_9.append(d2f_9)
    greska_9.append(error9)
for i in h_lista:
    d2f_10 = druga_derivacija(f,x=10,h=i)
    error10 = abs((d2f_10-numpy.exp(10))/(numpy.exp(10)))
    lista_x_je_10.append(d2f_10)
    greska_10.append(error10)
lista_derivacija = []
lista_derivacija2 = [lista_h_vrijednosti,lista_x_je_1,greska_1,lista_x_je_2,greska_2,lista_x_je_3,greska_3,lista_x_je_4,greska_4,lista_x_je_5,greska_5,lista_x_je_6,greska_6,lista_x_je_7,greska_7,lista_x_je_8,greska_8,lista_x_je_9,greska_9, lista_x_je_10,greska_10]
print(tabulate(lista_derivacija2))
greska_1.pop(0)
greska_5.pop(0)
greska_10.pop(0)
plt.xscale("log")
plt.yscale("Log")
plt.ylabel("log(error)")
plt.xlabel("log(h)")
plt.plot(lista_h_brojevi,greska_1)
plt.plot(lista_h_brojevi,greska_5)
plt.plot(lista_h_brojevi,greska_10)
plt.show()

        
