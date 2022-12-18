import matplotlib.pyplot as plt
import jednostavnonjihalo as nj
T = nj.analiticki_period()
a,b = nj.analiticki(4)
a_4,b_4,g,h = nj.rk4(4,0,0,7*T,2000)
a1,b1 = nj.analiticki(8)
a_8,b_8,g1,h1 = nj.rk4(8,0,0,7*T,2000)
a2,b2 = nj.analiticki(16)
a_16,b_16,g2,h2 = nj.rk4(16,0,0,7*T,2000)
a3,b3 = nj.analiticki(32)
a_32,b_32,g3,h3 = nj.rk4(32,0,0,7*T,2000)
a5,b5 = nj.analiticki(64)
a_64,b_64,g4,h4 = nj.rk4(64,0,0,7*T,2000)
plt.subplot(2,3,1)
plt.plot(a,b,c="r")
plt.plot(a_4,h,c="b")
plt.xlim(0,7*T)
plt.legend(["Analitički","RK4"],loc = "upper right")
plt.subplot(2,3,2)
plt.plot(a1,b1,c="r")
plt.plot(a_8,h1,c="b")
plt.xlim(0,7*T)
plt.legend(["Analitički","RK4"],loc = "upper right")
plt.subplot(2,3,3)
plt.plot(a2,b2,c="r")
plt.plot(a_16,h2,c="b")
plt.xlim(0,7*T)
plt.legend(["Analitički","RK4"],loc = "upper right")
plt.subplot(2,3,4)
plt.plot(a3,b3,c="r")
plt.plot(a_32,h3,c="b")
plt.xlim(0,7*T)
plt.legend(["Analitički","RK4"],loc = "upper right")
plt.subplot(2,3,5)
plt.plot(a5,b5,c="r")
plt.plot(a_64,h4,c="b")
plt.xlim(0,7*T)
plt.legend(["Analitički","RK4"],loc = "upper right")
plt.subplot(2,3,6)
b_ = []
for ž in range(0,len(b)):
    b_.append(b[ž]/4)
b4 = []
for z in range(0,len(b_4)):
    b4.append(b_4[z]/4)
b8 = []
for q in range(0,len(b_8)):
    b8.append(b_8[q]/8)
b16 = []
for č in range(0,len(b_16)):
    b16.append(b_16[č]/16)
b32 = []
for ć in range(0,len(b_32)):
    b32.append(b_32[ć]/32)
b64 = []
for š in range(0,len(b_64)):
    b64.append(b_64[š]/64)
plt.plot(a,b_,c="r")
plt.plot(a_4,b4,c="b")
plt.plot(a_8,b8,c="g")
plt.plot(a_16,b16,c="yellow")
plt.plot(a_32,b32,c="cyan")
plt.plot(a_64,b64,c="black")
plt.xlim(0,7*T)
plt.xlabel("t [s]")
plt.ylabel("y/y(0)")
plt.legend(["Analitičko","y(0)=4","y(0)=8","y(0)=16","y(0)=32","y(0)=64"],loc="lower left")
plt.show()
