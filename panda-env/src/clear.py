from app import df
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt 
df.drop(['Name', 'Lastname'], axis='columns', inplace=True)
df
df = df.drop_duplicates(['Name','Lastname'])
print(df.to_string())
# df = df.rename(columns={'nota Periodo III':'Nota Periodo III'})
# df
df.plot(kind='bar', x = 'Fullname', y = 'Average')
plt.show()
df.style.highlight_max()
df.style.background_gradient()