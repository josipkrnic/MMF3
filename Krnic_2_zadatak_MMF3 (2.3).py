import numpy as np
#Sustav linearnih jednadžbi za zadani problem glasi:
#Jed_1: R1*I1 + R2*(I1-I2) + R4*I1 = 5 V
#Jed_2: R1*I2 + R2*[I2-I3-(I1-I2)] + R4*I2 = 0
#Jed_3: R1*I3 + R2*[I3-I4-(I2-I3)] + R4*I3 = 0
#Jed_4: R1*I4 + R3*I4 - R2*(I3-I4) + R4*I4 = 0
#Izlučivanjem struja:
#Jed_1_sredena: (R1+R2+R4)*I1 - R2*I2 = 5
#Jed_2_sredena: -R2*I1 + (R1+2*R2+R4)*I2 - R2*I3 = 0
#Jed_3_sredena: -R2*I2 + (R1+2*R2+R4)*I3 - R2*I4 = 0
#Jed_4_sredena: -R2*I3 + (R1+R2+R3+R4)*I4 = 0
#Za zadane: R1 = 1 ohm, R2 = 2 ohm, R3 = 4 ohm i R4 = 1 ohm gornji sustav jest:
#Jed_1_broj: 4*I1 - 2*I2 = 5
#Jed_2_broj: -2*I1 + 6*I2 - 2*I3 = 0
#Jed_3_broj: -2*I2 + 6*I3 - 2*I4 = 0
#Jed_4_broj: -2*I3 + 8*I4 = 0
#Rješimo ovaj sustav:
a = [0,-2,-2,-2]
b = [4,6,6,8]
c = [-2,-2,-2,0]
d = [5,0,0,0]
N = len(a)
c_cc = np.zeros(N,dtype='float32')
d_cc = np.zeros(N,dtype='float32')
X = np.zeros(N, dtype='float32')
X_kon = np.zeros(N,dtype ='float32')
c_cc[0] = c[0]/b[0]
d_cc[0] = d[0]/b[0]
for i in range(1,N):
    c_cc[i] = (c[i])/(b[i]-a[i]*c_cc[i-1])
    d_cc[i] = (d[i]-a[i]*d_cc[i-1])/(b[i]-a[i]*c_cc[i-1])
X[(N-1)] = d_cc[N-1]
for j in range(N-2,-2,-1):
    X[j] = ((d_cc[j])-(c_cc[j]*X[j+1]))
    X_kon[j] = 94*X[j]
print("Iznosi struja I1,I2,I3 i I4 u amperima  su redom: ", X)
print("Ti isti iznosi pomnoženi s 94 zbog ljepšeg rješenja su: ", X_kon)
#with open(r'C:\Users\admin\Documents\Krnic_MMF3\struja.txt', 'w') as fp:
 #   for komponenta in X:
  #      fp.write("%s\n" % komponenta)
   # print("Ispisano")
