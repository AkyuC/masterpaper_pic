import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = 'SimSun'
plt.rcParams['font.serif'] = 'Times New Roman'
plt.rcParams['font.size'] = 15

plt.figure(figsize=(10,4))

lifetime = np.loadtxt("lifetime1.1-1.txt")

plt.plot(np.arange(len(lifetime)), lifetime, label="DRED")
plt.plot(np.arange(len(lifetime)), np.ones(len(lifetime))*2262, label='Greedy2')
plt.plot(np.arange(len(lifetime)), np.ones(len(lifetime))*2187, label='Greedy1')
plt.plot(np.arange(len(lifetime)), np.ones(len(lifetime))*1688, label='Random')

# 设置图表标题和坐标轴标签
plt.xlabel('训练回合数（episode）')
plt.ylabel('存活时间 / 轮')

plt.legend()

# 显示图形
plt.savefig("lifetime1.1-1.png", bbox_inches='tight', pad_inches=0.05, dpi=600)