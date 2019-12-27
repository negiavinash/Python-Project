from scipy.optimize import curve_fit 
from matplotlib import pyplot as plt 
from sklearn.metrics import confusion_matrix 
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report 
from math import sqrt
from sklearn.metrics import mean_squared_error
import pandas
import numpy 
df = pandas.read_csv('test.csv')
time = df.Time 
OutsideTemp = df.Outside_Temp 
InsideTemp = df.Inside_Temp

def test(OutsideTemp, a, b): 
    return a * OutsideTemp +b 

param, param_cov = curve_fit(test, OutsideTemp, InsideTemp) 

print(param)

predicted = (param[0]*OutsideTemp+param[1]) 
plt.plot(predicted,'r')
plt.plot(InsideTemp)

rmse = sqrt(mean_squared_error(InsideTemp, predicted))

print(rmse) 
