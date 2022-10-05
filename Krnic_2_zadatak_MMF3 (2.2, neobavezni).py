import numpy as np
a = [0,1,2,3,4,5,6]
b = [2,4,6,8,6,4,2]
c = [6,5,4,3,2,1,0]
d = [0,1,2,3,2,1,0]
N = len(a)
#N je broj redaka/stupaca
c_cc = np.zeros(N,dtype='float32')
d_cc = np.zeros(N,dtype='float32')
#cc je kao dvocrtano
X = np.zeros(N, dtype='float32')
#X je matrica rješenja sustava jednadžbi
c_cc[0] = c[0]/b[0]
d_cc[0] = d[0]/b[0]
for i in range(1,N):
    c_cc[i] = (c[i])/(b[i]-a[i]*c_cc[i-1])
    d_cc[i] = (d[i]-a[i]*d_cc[i-1])/(b[i]-a[i]*c_cc[i-1])
X[(N-1)] = d_cc[N-1]
for j in range(N-2,-1,-1):
    X[j] = ((d_cc[j])-(c_cc[j]*X[j+1]))
print("Rješenje sustava je: x = ",X)
