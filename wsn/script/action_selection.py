import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = 'SimSun'
plt.rcParams['font.serif'] = 'Times New Roman'
plt.rcParams['font.size'] = 15

plt.figure(figsize=(10,6))

actions = np.loadtxt("actionSelection")
yticks = [16,10,8,6,7,18,13,2,19,9,11,3,20,17,15,12,14,1,5,4] # 按照和中心的距离进行排序，16最近
m = {}
for i in range(20):
    m[yticks[i]] = i+1

for i in range(len(actions)):
    actions[i] = m[actions[i]]

plt.scatter(np.linspace(10, len(actions)*10, len(actions)), actions)

plt.xlabel('存活时间 / 轮')
plt.ylabel('悬停节点')
plt.yticks([i+1 for i in range(20)], yticks)

plt.savefig("action_selection.png", bbox_inches='tight', pad_inches=0.05, dpi=600)
plt.cla()

plt.figure(figsize=(10,4))
m = {1: 0, 2: 18, 3: 18, 4: 19, 5: 17, 6: 17, 7: 16, 8: 12, 9: 13, 10: 1, 11: 1, 12: 15, 13: 13, 14: 13, 15: 2, 16: 3, 17: 18, 18: 17, 19: 19, 20: 19}
x = [i+1 for i in range(20)]
print([m[i+1] for i in range(20)])
y = [m[yticks[i]] for i in range(20)]
plt.bar(x, y)

plt.xlabel('节点')
plt.ylabel('选作悬停节点的次数')
plt.xticks(x, yticks)
for i in range(len(x)):
    if y[i] <= 9:
        plt.text(i+0.86, y[i], str(int(y[i])))
    else:
        plt.text(i+0.7, y[i], str(int(y[i])))

plt.savefig("action_selection_count.png", bbox_inches='tight', pad_inches=0.05, dpi=600)
plt.cla()

# [8,4,6,5,7,14,18,12,13,17,2,20,19,3,9]，按照这个顺序选择，2249个存活时间