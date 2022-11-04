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
df.describe()
print("Sample: to choose random records")
df.sample(2)
df[2:9]#range
print("Iloc: loop DF")
df.iloc[3]
def clearData(name,lastname,mark1,mark2,mark3,mark4):
     print(f"Full name:  {name.upper()} {lastname.upper()} ")
     print(f"Grade1 {round(mark1,1)} ")
     print(f"Grade2 {round(mark2,2)} ")
     print(f"Grade3 {round(mark3,3)} ")
     print(f"Grade4 {round(mark4,4)} ")

for x in range(len(df)):
     name = str(df.iloc[x]["Name"])
     lastname = str(df.iloc[x]["Lastname"])
     mark1 = float(df.iloc[x]["Grade1"])
     mark2 = float(df.iloc[x]["Grade2"])
     mark3 = float(df.iloc[x]["Grade3"])
     mark4 = float(df.iloc[x]["Grade4"])
     clearData(name,lastname,mark1,mark2,mark3,mark4)     
