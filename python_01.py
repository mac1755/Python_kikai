import numpy as np
import time
from numpy.random import rand

#行、列の大きさ
N = 150

#行列を初期化する
matA = np.array(rand(N,N))
matB = np.array(rand(N,N))
matC = np.array([[0] * N for _ in range(N)])

#Pythonのリストを使って計算する
#開始時間を取得する
start = time.time()

#for文を使って行列のかけ算を実行する
for i in range(N):
    for j in range(N):
        for k in range(N):
            matC[i][j] = matA[i][k] * matB[k][j]

print("Pythonの機能のみでの計算結果:%.2f[sec]" % float(time.time() - start))

#Numpyを使って計算します。

matC = np.dot(matA, matB)

print("Numpyを使った場合の計算結果:%.2f[sec]" % float(time.time() - start))