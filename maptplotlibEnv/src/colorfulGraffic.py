import matplotlib.pyplot as plt
fig,ax = plt.subplots()
days=['L', 'M', 'X', 'J', 'V', 'S', 'D']
temperatures = {'Madrid':[28.5, 30.5, 31, 30, 28, 27.5, 30.5], 'Barcelona':[24.5, 25.5, 26.5, 25, 26.5, 24.5, 25]}
ax.plot(days,temperatures['Madrid'], color="tab:purple",marker = 'o',linestyle = 'dashed',label="Madrid")
ax.plot(days,temperatures['Barcelona'], color="tab:yellow",marker = '^',linestyle = 'doted',label="Barcelona")
ax.set_title('Daily temperature', loc = "left", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:green'})
ax.legend(loc = 'upper right')
plt.savefig("dispersion-diagram.png")
plt.show()