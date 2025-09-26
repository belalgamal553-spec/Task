import matplotlib.pyplot as plt
days = [1, 2, 3, 4, 5, 6, 7]
temperatures = [22, 21, 23, 27, 29, 24, 25]
plt.plot(days, temperatures, marker='o' , linestyle='-', color='green')
plt.title('Daily Temperatures Over a Week')
plt.xlabel('Days')
plt.ylabel('Temperature (°C)')
plt.show() 