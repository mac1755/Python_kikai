import numpy as np

x = np.array([1,2,3])

#arange(x) は値の要素をx個作成してくれます。
y = np.arange(5)

print(x)
print(y)

#1次元のndarrayクラス
array_1d = np.array([1,2,3,4,5,6,7,8])
print(array_1d)
#2次元のndarrayクラス
array_2d = np.array([[1,2,3,4],[5,6,7,8]])
print(array_2d)
#3次元のndarrayクラス
array_3d = np.array([[[1,2],[3,4],[5,6],[7,8]]])
print(array_3d)

#１次元配列の計算

#Numpyを使わないで実行した結果
'''
stoages = [1,2,3,4]
new_stages = []
for n in stoages:
    n += n
    new_stages.append(n)
print(new_stages)
'''
#Numpyを使って実行
storages = np.array([1,2,3,4])
storages += storages
print(storages)