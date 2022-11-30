def Lagrange(xa,ya,N,x):
    y = 0
    for i in range(N):
        li = 1
        for j in range(N):
            if j != i:
                li *=(x - xa[j])/(xa[i] - xa[j])
        y += ya[i]*li
    return y
