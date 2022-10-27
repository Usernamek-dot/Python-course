import pandas as pd
file = "Notas.xlsx"
df = pd.read_excel(file,sheet_name="Sheet1")
print(df)