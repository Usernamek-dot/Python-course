import matplotlib.pyplot as plt
from app import df
df.plot(kind = "bar" , x = "columnName", y ="columnName")
plt.show()
df[0:20].plot(kind = "bar" , x = "column1", y ="column2")

#graficar df mediante diagrama de barras.