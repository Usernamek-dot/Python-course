from app import df
df = df.drop_duplicates(["name"])  
print(df.to_string())
df["Full Name"] = df["Name"] + "  " + df["Lastname"]
df.drop(["Name","Lastname"],axis="columns",inplace=True)
df.duplicated["Name"]
df.plot(kind="bar",x="Fullname",y="Name")#pip install matplot
df.style.highlight_max()