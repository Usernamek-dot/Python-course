import matplotlib.pyplot as plt
from app import df
df[df["name"]]
df.style.highlight_max
df = df.sort_values("name")
df.background_gradient()