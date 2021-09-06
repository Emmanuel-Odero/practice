import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib import dates as mpl_dates
import random

plt.style.use('dark_background')

que = int(input("input the number of days you would like to plot"))

dates = [datetime(2019, 5, 1+d) for d in range(que)]

#convert dates from string to date formart to enable aligning
dates = pd.to_datetime(dates)

y = []
w = []

for x in range(que):
    y.append(random.randint(0,1000))
    
for x in range(que):
    w.append(random.randint(0,1000))
    
plt.plot_date(dates, y,color='red', linestyle='solid',label='bitcoin')
plt.plot_date(dates, w, linestyle='solid',label='yen')
plt.gcf().autofmt_xdate()

dateformart = mpl_dates.DateFormatter('%b, %d %y') #find out why this is giving an error

plt.fill_between(dates, y, w, alpha=0.25)
#plt.gca.xaxis.set_major_formatter(date_format)

plt.legend()

plt.title('Bitcoin Closing Prices')
plt.xlabel('Dates')
plt.ylabel('closiing price')

plt.tight_layout()
plt.show()