import matplotlib.pyplot as plt
fig,ax = plt.subplots()
ax.scatter(x=[1,2,3],y=[3,2,1])
# ax.plot([1, 2, 3, 4], [1, 2, 0, 0.5])
# ax.fill_between([1, 2, 3, 4], [1, 2, 0, 0.5])
#ax.bar([1, 2, 3], [3, 2, 1])
#ax.barh([1, 2, 3], [3, 2, 1])

# x = np.random.normal(5, 1.5, size=1000)
# ax.hist(x, np.arange(0, 11))

# ax.pie([5, 4, 3, 2, 1])
# ax.boxplot([1, 2, 1, 2, 3, 4, 3, 3, 5, 7])
# ax.violinplot([1, 2, 1, 2, 3, 4, 3, 3, 5, 7])

# x = np.linspace(-3.0, 3.0, 100)
# y = np.linspace(-3.0, 3.0, 100)
# x, y = np.meshgrid(x, y)
# z = np.sqrt(x**2 + 2*y**2)
# ax.contourf(x, y, z)

# x = np.random.random((16, 16))
# ax.imshow(x)

# x, y = np.random.multivariate_normal(mean=[0.0, 0.0], cov=[[1.0, 0.4], [0.4, 0.5]], size=1000).T
# ax.hist2d(x, y)

plt.savefig("dispersion-diagram.png")
plt.show()