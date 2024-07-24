import numpy as np

a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("matrix a is: \n",a)
b=np.array([[6,3,1],[7,1,1],[1,1,1]])
print("matrix b is:\n",b)
c=np.array([[0,0,0],[0,0,0],[0,0,0]])
print("addition of two matrices a &b is:\n",a+b)
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            c[i][j]+=a[i][k]*b[k][j]
print("multiplication of two matrices a&b is:\n")            
for r in c:
    print(r)

