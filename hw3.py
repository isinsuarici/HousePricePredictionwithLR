#libraries
import numpy as np
import pandas as pd

#data preprocessing steps
#data upload
veriler = pd.read_csv('prices.csv')
print(veriler)


#merging data and creating a dataframe (numpy arrays dataframe conversion)
price = veriler.iloc[:, 0]
valueof_y = pd.DataFrame(data=price, index=range(21613), columns=['price'])


values_except_price = veriler.iloc[:, 1:]
valueof_x = pd.DataFrame(data=values_except_price, index=range(21613), columns=['lot_area','living_area','num_floors', 'num_bedrooms','num_bathrooms','waterfront','year_built','year_renovated'])
print(valueof_x)

#division of data for training and testing
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(valueof_x,valueof_y,test_size=0.2, random_state=1)


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)
print(y_pred)

from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
print("MSE", mean_squared_error(y_test, y_pred))
score = r2_score(y_test, y_pred)
print('r2 score is ', score)
print('root_mean_squared error of is = ', np.sqrt(mean_squared_error(y_test,y_pred)))
