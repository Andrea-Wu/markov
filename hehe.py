import pandas as pd
import quandl, math
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression

df = quandl.get("WIKI/GOOGL")

#print(df.head())

df = df[['Adj. Open',  'Adj. High',  'Adj. Low',  'Adj. Close', 'Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Close'] * 100.0

df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

forecast_col = 'Adj. Close'
df.fillna(value=-99999, inplace=True)
forecast_out = int(math.ceil(0.01 * len(df)))

df['label'] =df[forecast_col].shift(-forecast_out)

df.dropna(inplace=True)
X = np.array(df.drop(['label'],1))
X = preprocessing.scale(X)
X_lately = x[-forecast_out:]
X= X[:forecast_out]

y = np.array(df['label'])
#X is all elements in matrix except for labels column
#y is all elements in labels column in its own array

#this scales all features on a scale of -1 to 1

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,y,test_size=0.2)
#returns training/testing sets of features and labels
#why are some of these things necessary?

#clf = svm.SVR()
#SVR = "support vector regression"

clf = LinearRegression()

clf.fit(X_train, y_train)
forecast_set = clf.predict(X_lately)

confidence = clf.score(X_test, y_test)

print(confidence)



#print(df.head())



