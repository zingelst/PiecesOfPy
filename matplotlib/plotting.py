# These are just snippets of how to do common things in matplotlib
# This was done in a Jupyter notebook so may not be the same in an
# IPython or other shell

#%matplotlib inline
import matplotlib.pyplot as plt
# Used for tick and axes formatting
# More info: https://matplotlib.org/stable/api/ticker_api.html#tick-formatting
from matplotlib.ticker import (MultipleLocator, 
                               FormatStrFormatter, 
                               AutoMinorLocator, FuncFormatter) 
# Make the figure larger since the Jupyter notebook default is a
# postage stamp
plt.rcParams['figure.figsize'] = [12, 8]
plt.rcParams['figure.dpi'] = 100

# Gets the curret figure and axes
fig = plt.gcf()
ax = plt.gca()

# Title and Axis labels
ax.set_title('Title ')
ax.set_xlabel('X Axis label') 
ax.set_ylabel('Y Axis label')

# Look here for info on Formatters: https://matplotlib.org/stable/api/ticker_api.html#tick-formatting
# Set the X axis formatter to a particular precision using FormatStrFormatter
ax.xaxis.set_major_formatter(FormatStrFormatter('% 1.2f'))
# Set the Y axis formatter to change the way it prints numbers on the axis
ax.yaxis.set_major_formatter(FuncFormatter(lambda x, p: format(int(x/1000000), ','))) 

# Stick some data on the plot (not loaded here, provide your own data)
ax.plot(data1, 'r.')
ax.plot(data2, 'g.')
ax.plot(data3, 'y.')

# Show a legend
ax.legend(('data1','data2','data3'))
