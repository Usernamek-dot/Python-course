import pandas as pd
df = pd.read_html("") 
print(type(pd))
print(df[1].info())