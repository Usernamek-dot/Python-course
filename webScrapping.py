import pandas as pd
df = pd.read_html("https://es.wikipedia.org/wiki/Anexo:Aglomeraciones_urbanas_m%C3%A1s_pobladas_del_mundo#Las_mayores_aglomeraciones_urbanas_de_Europa")
print(df[0].info())