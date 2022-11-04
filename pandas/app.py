import pandas as pd

archivo = '/content/drive/MyDrive/Notas.xlsx'
df = pd.read_excel(archivo, sheet_name="Hoja1" )
print(df)
df.shape
df.size
df.info()
df.head()
df.tail()
df.describe()
df.sample(5)
df[2:9]
df.iloc[3]
df.iloc[3]['Nota Periodo I']


def limpiardatos(nombre, apellido, nota1, nota2, nota3, nota4):
  print("Nombre completo:", nombre.upper(), apellido.upper())
  print("Nota1:", round(nota1, 1))
  print("Nota2:", round(nota2, 1))
  print("Nota3:", round(nota3, 1))
  print("Nota4:", round(nota4, 1))
  print()


for i in range(len(df)):
  nombre = str(df.iloc[i]['Nombre'])
  apellido = str(df.iloc[i]['Apellido'])
  nota1 = float(df.iloc[i]['Nota Periodo I'])
  nota2 = float(df.iloc[i]['Nota Periodo II'])
  nota3 = float(df.iloc[i]['nota Periodo III'])
  nota4 = float(df.iloc[i]['Nota Periodo IV'])

  limpiardatos(nombre, apellido, nota1, nota2, nota3, nota4)

#  for x in df:
#      df['Nombre'] = df['Nombre'].str.upper()
#      df['Apellido'] = df['Apellido'].str.upper()

print(df.to_string())
df = df.reindex(columns=['Nombre', 'Apellido', 'Nota Periodo I', 'Nota Periodo II','nota Periodo III','Nota Periodo IV', ])
df
df['Nota Periodo I'] = round(df['Nota Periodo I'], 1)
df['Nota Periodo II'] = round(df['Nota Periodo II'], 1)
df['nota Periodo III'] = round(df['nota Periodo III'], 1)
df['Nota Periodo IV'] = round(df['Nota Periodo IV'], 1)
df
df.mean(numeric_only=True)
df['Promedio'] = round((df['Nota Periodo I'] + df['Nota Periodo II'] + df['nota Periodo III'] + df['Nota Periodo IV'])/4, 1)
df
 


