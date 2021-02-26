#importing modules
from matplotlib import pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

#the machine learning model
prediction_year = int(input('Enter the year of prediction:'))
round(prediction_year)
data = pd.read_csv('Seats VS Years (CSV).csv')

#the bar graph
plt.title('The Model So Far')
plt.plot(data['Years'], data['Seats'], color='red')
plt.bar(data['Years'], data['Seats'], color='orange')
plt.grid()
plt.ylabel('No. of seats won')
plt.xlabel('Election Years')
plt.show()
print(data)
print('\n')

model = LinearRegression()
model.fit(data[['Years']], data[['Seats']])

if prediction_year < 2021:
    print('In the year of',prediction_year, 'BJP won (prediction):', model.predict([[prediction_year]]), 'seats.')
elif prediction_year > 2021:
    print('In the year of',prediction_year, 'BJP is going to win:', model.predict([[prediction_year]]), 'seats.')
elif prediction_year == 2021:
    print('In the year of',prediction_year, 'BJP is going to win:', model.predict([[prediction_year]]), 'seats.')
else:
    print(model.predict([[prediction_year]]))
