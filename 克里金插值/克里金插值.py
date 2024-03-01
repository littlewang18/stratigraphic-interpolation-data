import numpy as np
import pandas as pd
from math import *
from numpy.linalg import *
from pandas.core.common import flatten


np.set_printoptions(suppress=True)



# 读取数据
data = pd.read_csv('DATA.csv')
data = np.array(data)
data1 = pd.read_csv('randdata.csv')
data1 = np.array(data1)

# C0 = 50.0
# C = 150.0
# a = 1500

C0 = 660.88778488
C = 660.88778488
a = 3000.85287415

# 距离h
def dis(p1, p2):
    a1 = pow((pow((p1[0] - p2[0]), 2) + pow((p1[1] - p2[1]), 2)), 0.5)
    return a1


# 对应公式r(h)
def model(h):
    if h == 0:
        return 0
    elif h > 0:
        if h <= a:
            return C0 + C * (1.5 * h / a - 0.5 * pow(h, 3) / pow(a, 3))
        else:
            return C0 + C


finalResult = []
dict = {'predicted value': finalResult}


mytrain_data = data
mytrain_h = mytrain_data[:, 2].reshape(-1, 1)


for o in range(len(data1)):

    mytest_data = data1[o]
    K = np.ones((len(mytrain_data) + 1, len(mytrain_data) + 1))
    M = np.ones((len(mytrain_data) + 1, 1))

    for j in range(len(mytrain_data)):
        for k in range(len(mytrain_data)):
            temp = dis(mytrain_data[j], mytrain_data[k])
            if j == k:
                K[j][k] = C + C0
            else:
                K[j][k] = C + C0 - model(temp)

    for j in range(len(mytrain_data)):
        temp = dis(mytrain_data[j], mytest_data)
        M[j] = C + C0 - model(temp)

    K[len(K) - 1][len(K) - 1] = 0

    #Z = np.dot(inv(K), M)
    Z = np.dot(np.linalg.pinv(K), M)
    Z = np.delete(Z, len(Z) - 1, axis=0)

    result = np.dot(np.transpose(Z), mytrain_h)

    finalResult.append(result[0][0])

df = pd.DataFrame(dict)
df.to_csv('predicted.csv')
