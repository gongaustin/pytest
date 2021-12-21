import dataset as dt

from matplotlib import pyplot as plt

xs,ys = dt.get_beans(100)


plt.title("Size Toxicity Function",fontsize=12)
plt.xlabel("Bean Size")
plt.ylabel("Toxicity")
plt.scatter(xs,ys)



w = 0.5
alpha = 0.05 #学习率
for i in range(100):
    for i in range(100):
        x = xs[i]
        y = ys[i]
        #学习值
        y_pre = x * w
        #误差
        e = y - y_pre
        w = w + alpha * x * e

y_pre = xs*w

plt.plot(xs,y_pre)

plt.show()






