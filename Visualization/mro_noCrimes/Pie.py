import os
import csv
from nvd3 import pieChart
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    crimes = list(csv.reader(open('noCrimeOutput.txt', 'rb'), delimiter='\t'))

    chart = pieChart(name='pieChart', color_category='category20c', height=800, width=800)
    xdata = []
    ydata = []
    for crime in crimes:
        xdata.append(crime[0])
        ydata.append(crime[1])

    extra_serie = {"tooltip": {"y_start": "", "y_end": " counts"}}
    chart.add_serie(y=ydata, x=xdata, extra=extra_serie)
    chart.buildhtml()

    return chart.htmlcontent

port = os.getenv('VCAP_APP_PORT', '5004')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port), debug=True)