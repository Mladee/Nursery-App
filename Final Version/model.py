import pandas as pd


data = pd.read_csv('Final Data')
data = data.drop('Unnamed: 0', axis = 1)

X = data.drop('Class', axis = 1)
y = data['Class']

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state= 1)

from catboost import CatBoostClassifier

cat = CatBoostClassifier()

cat.fit(X_train,y_train)

import pickle

pickle.dump(cat, open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))