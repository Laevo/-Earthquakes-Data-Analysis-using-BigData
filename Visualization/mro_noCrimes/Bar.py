import os
import csv
from nvd3 import discreteBarChart
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    input_data = list(csv.reader(open('noCrimeOutput.txt', 'rb'), delimiter='\t'))
    chart = discreteBarChart(name='discreteBarChart', height=800, width=1800, margin_bottom=200, margin_top=40, margin_left=60, margin_right=60)
    crimes = []
    for row in input_data:
        if int(row[1])>=5:
            crimes.append([row[0], int(row[1])])
    xdata = []
    ydata = []
    crimes = sorted(crimes, key=lambda crimes: crimes[1], reverse=True)
    for place in crimes[:20]:
        xdata.append(place[0])
        ydata.append(place[1])

    chart.add_serie(y=ydata, x=xdata)
    chart.buildhtml()

    return chart.htmlcontent

port = os.getenv('VCAP_APP_PORT', '5000')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port), debug=True)