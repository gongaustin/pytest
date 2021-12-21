import dataset as dt

from matplotlib import pyplot as plt

xs,ys = dt.get_beans(100)


plt.title("Size Toxicity Function",fontsize=12)
plt.xlabel("Bean Size")
plt.ylabel("Toxicity")
plt.scatter(xs,ys)
plt.show()






