import os
import csv
from nvd3 import discreteBarChart

output = open('static/index.html', 'w')
input_data = list(csv.reader(open('noCrimeOutput.txt', 'rb'), delimiter='\t'))
chart = discreteBarChart(name='discreteBarChart', height=800, width=1800, margin_bottom=200, margin_top=40, margin_left=60, margin_right=60, xAxis_rotateLabels=-90)
crimes = []
for row in input_data:
    if int(row[1])>=5:
        crimes.append([row[0], int(row[1])])
xdata = []
ydata = []
crimes = sorted(crimes, key=lambda crimes: crimes[1], reverse=True)
# print crimes
for place in crimes:
    xdata.append(place[0])
    ydata.append(place[1])

chart.add_serie(y=ydata, x=xdata)
chart.buildhtml()

output.write(chart.htmlcontent)