import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = 'SimSun'
plt.rcParams['font.serif'] = 'Times New Roman'
plt.rcParams['font.size'] = 15

plt.figure(figsize=(10,4))

algStatic = [383.5, 395, 375] # node 12（从1开始）
algRandom = [1563.5, 1688, 1377]
algGreedy1 = [2177.6, 2209, 2158]
algGreedy2 = [2278.8, 2303, 2262]
DRED = [2507.1, 2527, 2479] # seed5, 41310

print((np.array([DRED[0]-algStatic[0], DRED[0]-algRandom[0], DRED[0]-algGreedy1[0], DRED[0]-algGreedy2[0]])/
       np.array([algStatic[0], algRandom[0], algGreedy1[0], algGreedy2[0]])).tolist())

x = ["Static", "Random", "Greedy1", "Greedy2", "DRED"]
y = np.array([algStatic[0], algRandom[0], algGreedy1[0], algGreedy2[0], DRED[0]])
error_up = np.array([algStatic[1], algRandom[1], algGreedy1[1], algGreedy2[1], DRED[1]])
error_down = np.array([algStatic[2], algRandom[2], algGreedy1[2], algGreedy2[2], DRED[2]])

y_mean = [algStatic[0], algRandom[0], algGreedy1[0], algGreedy2[0], DRED[0]]
for i in range(len(x)):
    plt.text(i-0.1, y_mean[i]+45, str(int(y_mean[i])))

# 绘制误差棒图
plt.errorbar(x, y, yerr=[y-error_down,error_up-y], fmt='ro', capsize=5)
plt.plot(x, y, 'bo-')

# 设置图表标题和坐标轴标签
plt.xlabel('算法')
plt.ylabel('存活时间 / 轮')

# 显示图形
plt.savefig("lifetimeEBRP100.png", bbox_inches='tight', pad_inches=0.05, dpi=600)