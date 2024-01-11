import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = 'SimSun'
plt.rcParams['font.serif'] = 'Times New Roman'
plt.rcParams['font.size'] = 15

plt.figure(figsize=(10,3))

lifetime = np.loadtxt("acoFinishTime")

x = np.arange(len(lifetime))
plt.plot(x, lifetime, label="ACO")
plt.plot(x, np.ones(len(lifetime))*279.5199, label="Option")
plt.ylabel("完成时间 / 秒")
plt.xlabel("迭代次数")
plt.tick_params(axis='x', length=6, width=2)
plt.tick_params(axis='y', length=6, width=2)
plt.legend()
plt.savefig("acoFinishTime.png", bbox_inches='tight', pad_inches=0.05, dpi=600)
plt.close('all')