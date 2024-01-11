import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = 'SimSun'
plt.rcParams['font.serif'] = 'Times New Roman'
plt.rcParams['font.size'] = 14

plt.figure(figsize=(10,3))

labels = ['5', '10', '15']
interval5 = [1974, 2259, 2360, 2548] # 1.8, seed5, best
interval10 = [1563, 2177, 2278, 2507] # 1.1, seed5, 41310
interval15 = [1574, 2114, 2208, 2423] # 1.9, seed4, best

DRED = [2548,2507,2423]
Greedy1 = [2259,2177,2114]
Greedy2 = [2360,2278,2208]
Random = [1974,1563,1574]

x = np.arange(len(labels))  # the label locations
width = 0.75  # the width of the bars

fig, ax = plt.subplots()

rects1 = ax.bar(x - 1.5*width/4, DRED, width/4, label='DRED')
rects2 = ax.bar(x - 0.5*width/4, Greedy1, width/4, label='Greedy1')
rects3 = ax.bar(x + 0.5*width/4, Greedy2, width/4, label='Greedy2')
rects4 = ax.bar(x + 1.5*width/4, Random, width/4, label='Random')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('存活时间 / 轮')
ax.set_ylim((1450,2650))
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_xlabel('决策间隔 / 轮')
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

plt.savefig("different_interval.png", bbox_inches='tight', pad_inches=0.05, dpi=600)
