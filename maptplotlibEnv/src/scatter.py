import matplotlib.pyplot as plt
from app import df
df.plot(kind = "scatter" , x = "columnName", y ="columnName")
plt.show()
df[0:20].plot(kind = "scatter" , x = "column1", y ="column2")
#graficar df mediante puntos de dirpersión.