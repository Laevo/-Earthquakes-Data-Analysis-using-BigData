import os
import csv
from nvd3 import lineChart
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    input_data = list(csv.reader(open('dateCrimeOutput.txt', 'rb'), delimiter='\t'))
    chart = lineChart(name="lineChart", x_is_date=False,  height=800, width=1800, margin_bottom=200, margin_top=40, margin_left=60, margin_right=60)
    crimes = []
    for row in input_data:
        crimes.append([row[0], row[1], int(row[2])])
    crimes = sorted(crimes, key=lambda crimes: ([crimes[0],crimes[1]]))

    xdata = []
    current_crime = None
    i = 0
    for crime in crimes:
        if str(crime[0]) == current_crime:
            xdata.append(crime[1])
            globals()['ydata%s' % i].append(crime[2])
        else:
            current_crime = crime[0]
            i = i+1
            globals()['name%s' % i] = str(crime[0])
            globals()['ydata%s' % i] = []
            xdata.append(str(crime[1]))
            globals()['ydata%s' % i].append(crime[2])

    kwargs1 = {'shape': 'circle', 'size': '20'}
    # kwargs2 = {'shape': 'cross', 'size': '4'}
    i = 1
    while True:
        try:
            chart.add_serie(name=globals()['name%s' % i], y=globals()['ydata%s' % i], x=xdata, **kwargs1)
            i = i + 1
        except:
            break

    chart.buildhtml()
    print chart.htmlcontent
    return chart.htmlcontent

port = os.getenv('VCAP_APP_PORT', '5007')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port), debug=True)