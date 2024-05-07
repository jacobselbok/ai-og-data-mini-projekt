import pandas as pd
import matplotlib.pyplot as plt

# Indlæst csv
df = pd.read_csv(r"Lektion 5\recipeData.csv")

# Dropper rows med manglende værdier
print(df.shape)
df.dropna(inplace=True)
print(df.shape)

# Tjekker info for at finde hvilke columns der har nummeriske værdier
print(df.info())

df["Size(L)"].plot.hist()
plt.show()

df["Color"].plot.hist()
plt.show()