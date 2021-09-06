from itertools import count
import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation


plt.style.use('dark_background')

x_val = []
y_val = []
index = count()


def animate(i):
    x_val.append(next(index))
    y_val.append(random.randint(0, 100))
    plt.cla() #clear axis, which prevents from color changin and maintans consitency
    plt.plot(x_val, y_val, color='red')
    
ani = FuncAnimation(plt.gcf(), animate, interval=1000)
    
plt.title('New York Stock Exchange')
plt.xlabel('Days')
plt.ylabel('Closing Price')
plt.show()