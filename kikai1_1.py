from sklearn.datasets import make_classification
import matplotlib.pyplot as plt
import matplotlib

#データ x 、ラベル y を生成します。
x , y = make_classification(n_samples=50, n_features=2, n_redundant=0, random_state=0)

#データの色付け、プロットの処理
plt.scatter(x[:, 0], x[:, 1], c=y, marker=".",
            cmap=matplotlib.cm.get_cmap(name="bwr"), alpha=0.7)
plt.grid(True)
plt.show()