from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_predict
from sklearn.datasets import load_boston
from sklearn.metrics import explained_variance_score, mean_squared_error
import numpy as np
import pylab as pl

boston = load_boston()
x = boston.data
y = boston.target
linereg = LinearRegression()
linereg.fit(x, y)
yp = linereg.predict(x)
yp_cv = cross_val_predict(linereg, x, y, cv = 10)

print('linreg.coef_ = ', linereg.coef_)
print('linreg.intercept_ = ', linereg.intercept_)