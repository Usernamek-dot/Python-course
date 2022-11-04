import pandas as pd
file= "./Notes.xlsx"
df = pd.read_excel(file,sheet_name="Sheet1")
print(df)
print("Shape: It tells dimensionality and number of elements in each dimesion.")
df.shape
print("Size: It tells size of element")
df.size
print("Info: It tells the details of data frame")
df.info()
print("Head: it shows first 5 results")
df.head()
print("Tail: it shows last 5 results")
df.tail()
print("Describe: It shows statistical information . It actually creates a DF")
print.describe()
print("Sample: to choose random records")
print.sample(2)
df[2:9]#range
print("Iloc: loop DF")
df.iloc[3]