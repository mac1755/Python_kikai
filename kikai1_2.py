from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

#データを生成します。
x, y = make_classification(n_samples=100, n_features=2, n_redundant=0, random_state=42)

#データを学習に使う分と評価の分に分けます。
train_x, test_x, train_y, test_y =train_test_split(x, y, random_state=42)

#モデルを構築します。
model = LogisticRegression(random_state=42)

#train_xとtrain_yを使ってモデルに学習させます。
model.fit(train_x, train_y)

#test_xに対するモデルの分類予測結果です。
pred_y = model.predict(test_x)
print(pred_y)