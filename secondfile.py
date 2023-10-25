import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('medata.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')

    for row in plots:
        x.append(row[0])
        y.append((row[1]))

plt.bar(x, y, color='g', width=0.72, label="ppw")
plt.xlabel('Week')
plt.ylabel('Points')
plt.title('Points scored by my fantasy football team each week')
plt.legend()
plt.show()

