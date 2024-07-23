from ML_TOOLS.models_ML import Regressor, Classifier, Cluster
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans


data = load_iris()
df = pd.DataFrame(data['data'])
df['target'] = data['target']
df0= df[df['target'] == 0]
df1 = df[df['target'] == 1]
df = pd.concat([df0, df1])
x_train, x_test, y_train, y_test = train_test_split(df.iloc[:, :-1], df['target'], random_state=42, shuffle=True, test_size=0.25)
model = Cluster(KMeans())
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
print(model.report(y_test, y_pred))
