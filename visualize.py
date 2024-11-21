# Visualize .csv data

import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("temperature_history.csv", names=["timestamp", "temperature"])
data["timestamp"] = pd.to_datetime(data["timestamp"])
data.set_index("timestamp", inplace=True)
data.plot()
plt.show()
