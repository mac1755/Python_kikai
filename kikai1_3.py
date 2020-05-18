import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

#データを生成します。
x, y = make_classification(n_samples=100, n_features=2, n_redundant=0, random_state=42)

train_x, test_x, train_y, test_y = train_test_split(x, y, random_state=42)

#モデルの構築
model = LogisticRegression()

#train_xとtrain_yを使って学習する
model.fit(train_x, train_y)

#test_xに対するモデルの分類予測結果を表示
pred_y = model.predict(test_x)

#生成したデータをプロットします。
plt.scatter(x[:, 0], x[:, 1], c=y, marker=".", cmap=matplotlib.cm.get_cmap(name="bwr"), alpha=0.7)


#学習させて導出した識別境界線をプロットします。
#model.coef_ はデータの各要素の重み（傾き）を
# model.intercept_ はデータの要素全部に対する修正（切片）を表します。
xi = np.linspace(-10, 10)
y = model.coef_[0][0] / model.coef_[0][1] * \
    xi - model.intercept_ / model.coef_[0][1]

plt.plot(xi, y)

#グラフのスケールを調整します。
plt.xlim(min(x[:, 0]) - 0.5, max(x[:, 0]) + 0.5)
plt.ylim(min(x[:, 1]) - 0.5, max(x[:, 1]) + 0.5)
plt.axes().set_aspect("equal", "datalim")

#グラフにタイトルを設定します。
plt.title("classification data using LogisticRegression")

# x軸、y軸それぞれに名前を設定します。
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()
