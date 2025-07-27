import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from CSV
df = pd.read_csv("dataset-rgb.csv")

# Plot
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x="Norm_R", y="Norm_G", hue="Tag", s=100)
plt.title("Normalized R vs G with Tags")
plt.grid(True)
plt.show()
