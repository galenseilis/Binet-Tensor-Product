import numpy as np
import matplotlib.pyplot as plt

def binet(X, Y):
    if len(X.shape) % 2 == 0:
        result = np.zeros(X.shape)
    else:
        result = np.zeros(X.shape[:-1])

    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                if len(X[i][k].shape) <= 2 and len(Y[k][j].shape) <= 2:
                    result[i][j] += np.dot(X[i][k], Y[k][j])
                else:
                    binet(X[i][k], Y[k][j])
    return result


x = np.random.random((3,3,3))
y = np.random.random((3,3,3))
pxy = binet(x,y)
print(pxy)
plt.imshow(pxy)
plt.show()
