import numpy as np

#input variables
a11,a12,a13,a14,b1 = [ int(x) for x in input().split()]
a21,a22,a23,a24,b2 = [ int(x) for x in input().split()]
a31,a32,a33,a34,b3 = [ int(x) for x in input().split()]
a41,a42,a43,a44,b4 = [ int(x) for x in input().split()]

#calculating determinant
determinant = np.array([[a11, a12, a13, a14], [a21, a22, a23, a24], [a31, a32, a33, a34], [ a41, a42, a43, a44]])
det_result=np.linalg.det(determinant)
#print(det_result)

#cheking the solution
if det_result==0:
    print(""Система не имеет решений"")
else:
    # calculating arrays
    M1 = np.array([[a11, a12, a13, a14], [a21, a22, a23, a24], [a31, a32, a33, a34], [ a41, a42, a43, a44]])  # Матрица (левая часть системы)
    v1 = np.array([b1, b2, b3, b4])  # Вектор (правая часть системы)
    r = np.linalg.solve(M1, v1)  # Находим решение системы
    print(r[0],r[1],r[2],r[3])
#print(a11,a12,a21,a22,b1,b2) 