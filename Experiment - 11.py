import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Experiment - 11.csv")
plt.plot(data['Range'], data['CSE1'])
plt.plot(data['Range'], data['CSE2'])
plt.title("Marks Distribution")
plt.xlabel("Range")
plt.ylabel("Number of Students")
plt.legend(["CSE1", "CSE2"])
plt.show()
