#import modules
from matplotlib import pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

#main machine learning bjpModel:


prediction_year = int(input('Prediction Year: '))#taking the input of the year that is to be predicted
print('\n')

bjpData = pd.read_csv('bjp_data(CSV).csv') #reading the BJP Data
congressData = pd.read_csv('congress_data(CSV).csv')#reading the Congress Data

#making the graph 
plt.scatter(bjpData['Years'], bjpData['Seats'], color = 'red') 
plt.scatter(congressData['Years'], congressData['Seats'], color = 'indigo') 
plt.plot(bjpData['Years'], bjpData['Seats'], color = 'orange')
plt.plot(congressData['Years'], congressData['Seats'], color = 'blue')
plt.title('The Model So Far...')
plt.ylabel('Seats Won')
plt.xlabel('Loksabha Election Years')
plt.legend(['This is BJP', 'This is AIC'])
plt.grid(color='pink')
plt.show()

#the machine-learning BJP Model
bjpModel = LinearRegression()
bjpModel.fit(bjpData[['Years']], bjpData[['Seats']])
prediction = bjpModel.predict([[prediction_year]])

#the machine-learning Congress Model
congressModel = LinearRegression()
congressModel.fit(congressData[['Years']], congressData[['Seats']])
congress_prediction = congressModel.predict([[prediction_year]])

#showing the BJP Data
print('The BJP Data...\n')
print(bjpData)
print('\n')

#creating another divider
print('---------------------------------------------------------------------------')
print('\n')

#showing the Congress Data
print('The Congress Data...\n')
print(congressData)
print('\n')

#creating a divider
print('---------------------------------------------------------------------------')
print('/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/')
print('---------------------------------------------------------------------------')

#if-else statements of BJP Model
if prediction_year == 2021:
    print('\n')
    print('In the year of', prediction_year,',', 'BJP is going to win (parliamentary):', prediction, 'seats.')
elif prediction_year > 2021:
    print('\n')
    print('In the year of', prediction_year,',',  'BJP is going to win (prediction):', prediction, 'seats')
elif prediction_year < 2021:
    print('\n')
    print('In the year of', prediction_year,',','BJP won (prediction):', prediction, 'seats')
else:
    print('Invalid Inputs! Something Went Wrong!')

#if-else statments of the Congress Model:
if prediction_year == 2021:
    print('\n')
    print('In the year of', prediction_year,',', 'Congress is going to win (parliamentary):', congress_prediction, 'seats')
elif prediction_year > 2021:
    print('\n')
    print('In the year of', prediction_year,',',  'Congress is going to win (prediction):', congress_prediction, 'seats')
elif prediction_year < 2021:
    print('\n')
    print('In the year of', prediction_year,',','Congress won (prediction):', congress_prediction, 'seats')
else:
    print('Invalid Inputs! Something Went Wrong!')
