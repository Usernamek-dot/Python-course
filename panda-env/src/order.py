from app import df
df.reindex(columns=["Name","Lastname","Note1","Note2","Note3","Note4"])
df["Note1"]=round(df["Note1"],1)
df["Note2"]=round(df["Note2"],1)
df["Note3"]=round(df["Note3"],1)
df["Note4"]=round(df["Note4"],1)
df["Average"] =round((df['Note1'] + df['Note2'] + df['Note3'] + df['Note4'])/4, 1)
print(df)
