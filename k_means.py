#!/usr/bin/env python
import matplotlib.pyplot as plt
import csv
import random
import math
def read_csv(filename):
   coordinates = []
   with open(filename) as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      for row in csv_reader:
         coordinates.append(list(row))
   return coordinates

def perform_kms(dataset, centroid1, centroid2):
       c1 = []
       c2 = []
       for coordinate in dataset:
              dc1 = math.sqrt(math.pow((coordinate[1]-centroid1[0]),2)+math.pow((coordinate[2]-centroid1[1]), 2))
              dc2 = math.sqrt(math.pow((coordinate[1]-centroid2[0]),2)+math.pow((coordinate[2]-centroid2[1]), 2))
              if dc1 <= dc2:
                     c1.append(coordinate)
                    # print("Added to cluster 1")
              else:
                     c2.append(coordinate)
                    # print("Added to cluster 2")
       return c1,c2

   
def calc_centroid(cluster):
       if len(cluster) == 0:
              return [0,0]
       (x,y) = (0.0,0.0)
       for coordinate in cluster:
              x = x + coordinate[1]
              y = y + coordinate[2]
       x = x / len(cluster)
       y = y / len(cluster)
       return [x,y]


s = "kms.csv"
l = read_csv(s)
kms_dataset = []
for row in l:
       temp = [float(x) for x in row]
       kms_dataset.append(temp)


c1 = [random.random(),random.random()]
c2 = [random.random(),random.random()]


cluster1 = []
cluster2 = []
cluster1, cluster2 = perform_kms(kms_dataset, c1, c2)



c1 = calc_centroid(cluster1)
c2 = calc_centroid(cluster2)




k = int(input("Enter k:"))
for i in range(k):
       cluster1,cluster2 = perform_kms(kms_dataset, c1, c2)
       c1 = calc_centroid(cluster1)
       c2 = calc_centroid(cluster2)




print("cluster1=\n",cluster1)
print("cluster2=\n", cluster2)


plt.plot([x[1] for x in cluster1], [x[2] for x in cluster1], "ro")
plt.plot([x[1] for x in cluster2],[x[2] for x in cluster2], "bo")
plt.show()

