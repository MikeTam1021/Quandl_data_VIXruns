"""
Created on Tue Oct 27 14:14:14 2015

@author: MikeTam
"""

import Quandl
import pandas as pd
import matplotlib.pyplot as plt

data = Quandl.get('FED/RILSPDEPM03_N_WF', authtoken='xxxxxx', trim_start='1972-01-01', trim_end='1993-01-01')
data["movavg"] = pd.stats.moments.rolling_mean(data["Value"], 20)

top = plt.subplot2grid((4,4), (0,0), rowspan=3, colspan=4)
top.plot(data.index, data["Value"])
top.plot(data.index, data["movavg"])
plt.title('Eurodollars price 1972-1992')
