import time
import math
import sys
import numpy as np
from sklearn.cluster import KMeans
import csv
from nvd3 import scatterChart

start_time = time.time()
field1 = int(sys.argv[1])
field2 = int(sys.argv[2])
num_clusters = int(sys.argv[3])
X = []
output = open("/var/www/html/clstr/static/clusterview.html", "w")
data = csv.reader(open("/var/www/html/clstr/static/quakes.csv","r"), skipinitialspace=True)
first_line = True
for line in data:
    if first_line:
        first_line = False
    else:
        try:
            hor = float(line[field1])
            dep = float(line[field2])
            X.append([hor, dep])
        except:
            pass
X = np.asarray(X)
#X = X[:400]

kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(X)
centroids = kmeans.cluster_centers_
labels = kmeans.labels_

chart = scatterChart(name='scatterChart',margin_top=70, margin_bottom=200, height=800, width=1800)

for j in range(0, num_clusters):
    globals()['centx%s' % j] = []
    globals()['centy%s' % j] = []
for i in range(len(labels)):
    for j in range(0,num_clusters):
        if labels[i:i+1] == j:
            globals()['centx%s' % j].append(X[i][0])
            globals()['centy%s' % j].append(X[i][1])

kwargs1 = {'shape': 'cross', 'size': '20', 'color': 'black'}
for c in range(0, num_clusters):
    groupName = str('Cluster%s' % str(c+1))
    chart.add_serie(name=groupName, y=globals()['centy%s' % c], x=globals()['centx%s' % c])
chart.add_serie(name="Centroids", y=centroids[:, 1], x=centroids[:, 0], **kwargs1)
chart.buildhtml()
output.write(chart.htmlcontent)
print("--- %s seconds ---" % (time.time() - start_time))
