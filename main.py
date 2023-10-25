import matplotlib.pyplot as plt

x = []
y = []
z =[]
import csv

with open('mydata.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')

    for row in plots:
        x.append(row[0])
        y.append((row[1]))
        z.append((row[2]))

plt.plot(x, y,z, marker='o', markerfacecolor='r')

plt.show()


