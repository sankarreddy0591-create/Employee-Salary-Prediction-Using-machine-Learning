
# # import liquired libraries
import numpy as np
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

# # loading the data dataset into a pandas
data=pd.read_excel("data/Employees.xlsx")
print("dataset loaded successfully!")

# # the first five records in the data
print("\nFirst 5 records :")
print(data.head())

# # the last five records in the data
print("\nLast 5 ecords:")
print(data.tail())

# # finding the number of rows and columns
print("\nDataset shpe:")
print(data.shape)

# # check the minimum statistical reports in the data
print("\nStatistical summary:")
data.info()

# # finding the missing or null values in the data
print("\nMissing values:")
print(data.isna().sum())

# # finding the duplicates in the data
print("\nNumber of duplicate rows:")
print(data.duplicated().sum())

# #check the column names in the data
print("\nColumn names:")
print(data.columns)

# select feature columns
x=data[['Years','Job Rate']]
print("\nFeatues x:")

# to see the features "x"
print(x)

# select target column
y=data["Monthly Salary"]
print("\nTarget y:")

# to see the target "y"
print(y)

# import required  the model train_test_split
from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y, test_size=0.2, random_state=42)

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

# the model LogisticRegression()
from sklearn.linear_model import LinearRegression

#create model
lr=LinearRegression()

#trin model
lr.fit(x_train,y_train)

# make prediction
y_pred=lr.predict(x_test)

# Actual vs Pediction
comparison=pd.DataFrame({
    'Actual Salaries':y_test.values,
    'Predicted':y_pred
})
print(comparison.head(10))

# import model evalution mean_absolute_error,mean_squared_error

from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score,root_mean_squared_error

# Evaluation model
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("RMSE:", root_mean_squared_error(y_test, y_pred))
print("R2:", r2_score(y_test,y_pred))

##

import os
os.makedirs("../model", exist_ok=True)

import joblib
joblib.dump(lr,"../model/linearmodel.pkl")
print("Linear egression model saved successfully!")
