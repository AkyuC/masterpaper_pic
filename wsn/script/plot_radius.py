import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = 'SimSun'
plt.rcParams['font.serif'] = 'Times New Roman'
plt.rcParams['font.size'] = 15

plt.figure(figsize=(10,4))

x = [ 60 + i*10 for i in range(10)]
y = [890.8, 1805, 1892, 2304, 2503, 2513, 2548, 2603, 2597, 2629]
error_up = np.array([953, 1848, 1917, 2329, 2538, 2557, 2589, 2639, 2657, 2689])
error_down = np.array([848, 1768, 1849, 2259, 2478, 2479, 2489, 2559, 2524, 2549])

for i in range(len(x)):
    plt.text(x[i], int(y[i])+20, str(int(y[i])))

# 绘制误差棒图
plt.errorbar(x, y, yerr=[y-error_down,error_up-y], fmt='ro', capsize=5)
plt.plot(x, y, 'bo-')

plt.xticks(x,x)

# 设置图表标题和坐标轴标签
plt.xlabel('通信范围 / 米')
plt.ylabel('存活时间 / 轮')

# 显示图形
plt.savefig("same_model_diff_radius.png", bbox_inches='tight', pad_inches=0.05, dpi=600)

plt.cla()

plt.figure(figsize=(10,3))
labels = ['70', '100', '130']
interval5 = [1394, 1518, 1663, 1872] # 1.10, seed3, best
interval10 = [1563, 2177, 2278, 2507] # 1.1, seed5, 41310
interval15 = [1778, 2437, 2613, 2723] # 1.9, seed4, best

DRED = [1872,2507,2723]
Greedy1 = [1518,2177,2437]
Greedy2 = [1663,2278,2613]
Random = [1394,1563,1778]

x = np.arange(len(labels))  # the label locations
width = 0.75  # the width of the bars

fig, ax = plt.subplots()

rects1 = ax.bar(x - 1.5*width/4, DRED, width/4, label='DRED')
rects2 = ax.bar(x - 0.5*width/4, Greedy1, width/4, label='Greedy1')
rects3 = ax.bar(x + 0.5*width/4, Greedy2, width/4, label='Greedy2')
rects4 = ax.bar(x + 1.5*width/4, Random, width/4, label='Random')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('存活时间 / 轮')
ax.set_ylim((1350,2830))
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_xlabel('通信范围 / 米')
ax.legend(loc='upper center', bbox_to_anchor=(0.47, 1.15), ncol=4, fontsize=13)


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 5),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=12)


autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)

fig.tight_layout()

plt.savefig("diff_model_diff_radius.png", bbox_inches='tight', pad_inches=0.05, dpi=600)