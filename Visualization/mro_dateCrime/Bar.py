import os
import csv
from nvd3 import multiBarChart
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    output = open('static/index.html', 'w')
    input_data = list(csv.reader(open('dateCrimeOutput.txt', 'rb'), delimiter='\t'))
    chart = multiBarChart(name='multiBarChart', height=800, width=1800, margin_bottom=300, margin_top=40, margin_left=60, margin_right=60)
    crimes = []
    for row in input_data:
        crimes.append([row[0], int(row[1]), int(row[2])])
    crimes = sorted(crimes, key=lambda crimes: crimes[1], reverse=True)
    current_year = None
    i = 0
    for crime in crimes:
        if crime[1] == current_year:
            globals()['xdata%s' % i].append(crime[0])
            globals()['ydata%s' % i].append(crime[2])
        else:
            current_year = crime[1]
            i = i+1
            globals()['year%s' % i] = str(crime[1])
            globals()['ydata%s' % i] = []
            globals()['xdata%s' % i] = []
            globals()['ydata%s' % i].append(crime[2])
            globals()['xdata%s' % i].append(crime[0])


    i = 1
    while True:
        try:
            kwargs1 = {'key': globals()['year%s' % i]}
            chart.add_serie(name=globals()['year%s' % i], y=globals()['ydata%s' % i], x=globals()['xdata%s' % i], **kwargs1)
            i = i + 1
        except:
            break
    chart.buildhtml()
    output.write(chart.htmlcontent)
    return chart.htmlcontent

port = os.getenv('VCAP_APP_PORT', '5010')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port), debug=True)