import matplotlib.pyplot as plt
fig,ax = plt.subplots()
days=['L', 'M', 'X', 'J', 'V', 'S', 'D']
temperatures = {'Madrid':[28.5, 30.5, 31, 30, 28, 27.5, 30.5], 'Barcelona':[24.5, 25.5, 26.5, 25, 26.5, 24.5, 25]}
ax.plot(days,temperatures['Madrid'], color="tab:purple")
ax.plot(days,temperatures['Barcelona'], color="tab:yellow")
ax.plot(days,temperatures['Madrid'], marker = 'o')
ax.plot(days,temperatures['Barcelona'], marker = '^')
ax.plot(days,temperatures['Madrid'], linestyle = 'dashed')
ax.plot(days,temperatures['Barcelona'], linestyle = 'doted')
ax.set_title('Daily temperature', loc = "left", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:green'})
plt.savefig("dispersion-diagram.png")
plt.show()