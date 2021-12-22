#代价函数

import dataset
import numpy as np
from matplotlib import pyplot as plt


#获取样本数据
xs,ys = dataset.get_beans(100)

plt.title("cost_function",fontsize=12)
plt.xlabel("w")
plt.ylabel("squared error")

#设定w初始值

#生成w的数组






#初始关系值
w = 0.5

#估计值

y_pre = w*xs;


#误差
e = ys-y_pre

#方差
es = e**2
#方差和
sum_es = np.sum(es)

#平方均差

aver_es = sum_es/100;

print(aver_es)





ws = np.arange(0,3,0.1)
aver_es = []
#定义一个数组接收

for w in ws:
    aver_e = (1/100)*np.sum((ys-xs*w)**2)
    aver_es.append(aver_e)

plt.plot(ws,aver_es)

plt.show()

#计算误差最小值时w的值(-b/2a)

w_min = np.sum(xs*ys)/np.sum(xs*xs)

print('w_min='+str(w_min))