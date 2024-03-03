import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = 'SimSun'
plt.rcParams['font.serif'] = 'Times New Roman'
plt.rcParams['font.size'] = 15

plt.figure(figsize=(10,4))

lifetime1_1 = np.loadtxt("lifetime1.1-1.txt")
lifetime1_6 = np.loadtxt("lifetime1.6-5")

plt.plot(np.arange(len(lifetime1_1)), lifetime1_1, label="DRED")
plt.plot(np.arange(len(lifetime1_1)), lifetime1_6[:len(lifetime1_1)], label="DRED with Location")

# 设置图表标题和坐标轴标签
plt.xlabel('训练回合数（episode）')
plt.ylabel('存活时间 / 轮')

plt.legend()

# 显示图形
plt.savefig("lifetime_compare_loc.png", bbox_inches='tight', pad_inches=0.05, dpi=600)