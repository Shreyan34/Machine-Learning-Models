#main machine learning model:
prediction_year = int(input('Prediction Year: '))#taking the input of the year that is to be predicted

data = pd.read_csv('seats_vs_years(CSV).csv') #reading the data

#making the graph
plt.scatter(data['Years'], data['Seats'], color = 'red') 
plt.plot(data['Years'], data['Seats'], color = 'orange')
plt.title('The Model So Far...')
plt.ylabel('Seats Won')
plt.xlabel('Loksabha Election Years')
plt.grid()
plt.show()

#the machine-learning model
model = LinearRegression()
model.fit(data[['Years']], data[['Seats']])
prediction = model.predict([[prediction_year]])

#showing the data
print(data)
print('\n')

#creating a divider
print('---------------------------------------------------------------------------')
print('/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/')
print('---------------------------------------------------------------------------')

#if-else statements
if prediction_year == 2021:
    print('\n')
    print('In the year of', prediction_year,',', 'BJP is going to win (parliamentary):', prediction, 'seats')
elif prediction_year > 2021:
    print('\n')
    print('In the year of', prediction_year,',',  'BJP is going to win (prediction):', prediction, 'seats')
elif prediction_year < 2021:
    print('\n')
    print('In the year of', prediction_year,',','BJP won (prediction):', prediction, 'seats')
else:
    print('Invalid Inputs! Something Went Wrong!')
