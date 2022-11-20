from products import df
def readRecord(name,lastname,mark1,mark2,mark3,mark4):
     print(f"Full name:  {name.upper()} {lastname.upper()} ")
     print(f"Grade1 {round(mark1,1)} ")
     print(f"Grade2 {round(mark2,2)} ")
     print(f"Grade3 {round(mark3,3)} ")
     print(f"Grade4 {round(mark4,4)} ")

for x in range(len(df)):
     name = str(df.iloc[x]["Name"])
     lastname = str(df.iloc[x]["Lastname"])
     mark1 = float(df.iloc[x]["Note1"])
     mark2 = float(df.iloc[x]["Note2"])
     mark3 = float(df.iloc[x]["Note3"])
     mark4 = float(df.iloc[x]["Note4"])
     readRecord(name,lastname,mark1,mark2,mark3,mark4)     
