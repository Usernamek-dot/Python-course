tuple = (3.4,400,"value3",False)
subTuple=["iitem","item2","item3"]
tuple.add(subTuple)
print(type(tuple))
print(tuple[3])
print(f"The tuple size is {len(tuple)} ")
print(tuple.index(400))