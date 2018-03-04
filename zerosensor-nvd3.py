# zerosensor nvd3
# nwgat.ninja

import sqlite3
from nvd3 import lineChart

# fetch sensor data from sqlite
c = sqlite3.connect('sensor.db')

# print temperature
cur = c.cursor()
cur.execute("SELECT temp from data")
temp = cur.fetchall()
print temp

# print humidity
cur = c.cursor()
cur.execute("SELECT hum from data")
hum = cur.fetchall()
print hum

# print unixtime
cur = c.cursor()
cur.execute("SELECT ut from data")
ut = cur.fetchall()
print ut

# Open File to write the D3 Graph
output_file = open('html/index.html', 'w')

chart = lineChart(name="lineChart", x_is_date=False, x_axis_format="AM_PM")

xdata = range(24)
ydata = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
ydata2 = [18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18]

extra_serie = {"tooltip": {"y_start": "There are ", "y_end": " calls"}}
chart.add_serie(y=ydata, x=xdata, name='Temperature', extra=extra_serie,)
extra_serie = {"tooltip": {"y_start": "", "y_end": " min"}}
chart.add_serie(y=ydata2, x=xdata, name='Humidity', extra=extra_serie,)
chart.buildhtml()
output_file.write(chart.htmlcontent)

# close Html file
output_file.close()
