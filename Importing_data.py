import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression


# Load the CSV file into a NumPy array
Air_sensor1 = pd.read_csv('T_FLOW_SCC_1YMD1.csv')
Air_sensor2 = pd.read_csv('T_FLOW_SCC_1YMD2.csv')
Air_sensor3 = pd.read_csv('T_FLOW_SCC_1YPD1.csv')
Air_sensor4 = pd.read_csv('T_FLOW_SCC_1YPD3.csv')


# plot the data from sensor 1
print(Air_sensor1.head())
Time = Air_sensor1['Time']
TFlow = Air_sensor1['Traffic Flow (cars/min)']
plt.figure()
plt.plot(Time,TFlow,linewidth=0.5)
plt.xlabel("Time")
plt.ylabel("Traffic Flow (cars/min)")
plt.title("Sensor 1")
plt.grid()

# plot data from sensor 2
print(Air_sensor2.head())
Time2 = Air_sensor2['Time']
TFlow2 = Air_sensor2['Traffic Flow (cars/min)']
plt.figure()
plt.plot(Time2,TFlow2,linewidth=0.5)
plt.xlabel("Time")
plt.ylabel("Traffic Flow (cars/min)")
plt.title("Sensor 2")
plt.grid()

# plot the data from sensor 3
print(Air_sensor3.head())
Time3 = Air_sensor3['Time']
TFlow3 = Air_sensor3['Traffic Flow (cars/min)']
plt.figure()
plt.plot(Time3,TFlow3,linewidth=0.5)
plt.xlabel("Time")
plt.ylabel("Traffic Flow (cars/min)")
plt.title("Sensor 3")
plt.grid()

# plot data from sensor 4
print(Air_sensor4.head())
Time4 = Air_sensor4['Time']
TFlow4 = Air_sensor4['Traffic Flow (cars/min)']
plt.figure()
plt.plot(Time4,TFlow4,linewidth=0.5)
plt.xlabel("Time")
plt.ylabel("Traffic Flow (cars/min)")
plt.title("Sensor 4")
plt.grid()
plt.show()