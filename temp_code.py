from threading import Thread
import matplotlib.pyplot as plt
import pandas as pd
from time import sleep
fig=plt.figure()
class PlotThread(Thread):
    def run(self):
        data = pd.read_csv('C:\\Users\\HP\\New folder\\flightSimulatorResults.csv')
        x_axis1 = data['Time']
        y_axis1 = data['Velocity']
        y_axis2 = data['Acceleration']
        y_axis3 = data['Altitude']
        y_axis4 = data['Thrust']
        ax1=fig.add_subplot(221)
        ax2=fig.add_subplot(222)
        ax3=fig.add_subplot(223)
        ax4=fig.add_subplot(224)
        ax1.set_xlabel('Time')
        ax1.set_ylabel('Velocity')
        ax2.set_xlabel('Time')
        ax2.set_ylabel('Acceleration')
        ax3.set_xlabel('Time')
        ax3.set_ylabel('Altitude')
        ax4.set_xlabel('Time')
        ax4.set_ylabel('Thrust')
        for i in range(len(x_axis1)):
            ax1.plot(x_axis1[:i], y_axis1[:i], 'r-')
            ax2.plot(x_axis1[:i], y_axis2[:i], 'g-')
            ax3.plot(x_axis1[:i], y_axis3[:i], 'b-')
            ax4.plot(x_axis1[:i], y_axis4[:i], 'y-')
            sleep(0.1)
            plt.draw()
        plt.tight_layout()
self=PlotThread()
self.start()
plt.pause(100)
self.join()
plt.show()
