import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from cycler import cycler

#This file is for testing, changes made here are not automatically transferred to the stylesheet and have to be manually set there aswell. 

# If you wish to change your default style, copy the stylesheet to one of the
# following locations:
#     Unix/Linux:
#         $HOME/.config/matplotlib/matplotlibrc OR
#         $XDG_CONFIG_HOME/matplotlib/matplotlibrc (if $XDG_CONFIG_HOME is set)
#     Other platforms:
#         $HOME/.matplotlib/matplotlibrc


# Create some test data to plot

x = np.linspace(0,100,100)
y = np.random.rand(100)
y2 = np.random.randn(100)
y3 = np.random.randn(100)
y4 = np.random.randn(100)
#Colors https://personal.sron.nl/~pault/ Vibrant





plt.style.use('E:/Daten/Code/MatPlotLib StyleSheet/myStyle.mlpstyle')
fig, ax = plt.subplots()
ax.set_title("Title")
ax.plot(x,y)
ax.plot(x,y2)
ax.plot(x,y3)
ax.plot(x,y4)
ax.set_xlabel("X-Axis")
ax.set_ylabel("Y-Axis")
plt.show()