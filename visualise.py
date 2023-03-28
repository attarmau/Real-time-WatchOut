import pandas as pd
import matpllotlib .pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')
def animate(i):
  data = pd.read_csv('data.csv')
  x = range(len(data['Time']))
  y1 = data['HR']
  y2 = data['SpO2']
  plt.cla()
  plt.plot(x, y1, label = 'HR')
  plt.plot(x, y2, label = 'SpO2')
  plt.legend(loc='lower right')
ani = FuncAnimation(plt.gcf(), animate, interval = 1000)
plt.show()
