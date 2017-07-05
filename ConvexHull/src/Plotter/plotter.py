import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import pandas as pd
import numpy as np

x = []
y = []
hx = []
hy = []

# reading the file
df = pd.read_csv('exercise-1.csv', delimiter=',', skipinitialspace=True) #"exercise-1.csv" is the file name for exercise, must change for every exercise
x.extend(np.around(df['x'], decimals=2))  # assigning the first column values to the array
y.extend(np.around(df['y'], decimals=2))  # assigning the second column values to the array

for line in open("pointsFile.txt"): #dont have to change filename "pointsFile.txt"
    columns = line.split(' ')
    hx.append(columns[0])
    hy.append(columns[1])

extra1 = hx[0]
extra2 = hy[0]
hx.append(extra1)
hy.append(extra2)

# plotting
plt.plot(x, y, 'b.', marker='.', markersize=10)
plt.plot(hx, hy, 'r.-', marker='.', markersize=10)
plt.title('Convex Hull')
plt.show()