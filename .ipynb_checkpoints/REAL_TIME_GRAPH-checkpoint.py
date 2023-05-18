import random
from itertools import count
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('fivethirtyeight')
x_vals=[]
y_vals=[]
index=count()#counts one number at a time and we get next value everytime.
def animate(i):
    data=pd.read_csv('flightSimulatorResults.csv')
    x=data['Time']
    y=data['Velocity']
    plt.cla()
    plt.plot(x,y1,label='SIMULATION')
    plt.legend(loc='upper right')
    plt.tight_layout()

    
ani=FuncAnimation(plt.gcf(),animate,interval=1000,cache_frame_data=False)
plt.tight_layout()
plt.show()
ani.save("REALTIME.png")

