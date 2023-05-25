import numpy as np

def no_numpy_mult(first, second):
    r=[]
    result=[]
    for i in range(len(first)):
        for j in range(len(second[0])):
            sums=0
            for k in range(len(second)):
                sums=sums+(first[i][k]*second[k][j])
            r.append(sums)
        result.append(r)
        r=[]
    return result
    
    for i in range(len(first)):
        for j in range(len(second[0])):
            for k in range(len(second)):
                result[i][j] += first[i][k] * second[k][j]
    return result

def numpy_mult(first, second):
    return np.dot(first,second)
 