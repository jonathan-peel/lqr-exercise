import csv
import pandas
import matplotlib.pyplot as plt

with open("./notebooks/default_control.csv") as file:
    data = pandas.read_csv(file)
    control_inputs = data['u']

# lets us look at the distribution of the default control inputs
plt.hist(control_inputs)
plt.show()
