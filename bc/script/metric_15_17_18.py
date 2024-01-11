import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = 'SimSun'
plt.rcParams['font.serif'] = 'Times New Roman'
plt.rcParams['font.size'] = 15

plt.figure(figsize=(10,3))

avg_finished_time = np.loadtxt("avg_finished_time7.0")

datalen = 2010 if len(avg_finished_time) > 2010 else len(avg_finished_time)

plt.plot(np.arange(datalen), avg_finished_time[:datalen], label="Ours", linewidth = 2)
plt.plot(np.arange(datalen), np.ones(datalen)*279.1661, label="Option", alpha = 0.75, linewidth = 2)
plt.plot(np.arange(datalen), np.ones(datalen)*362.6101, label="Nearest", alpha = 0.75, linewidth = 2)
plt.plot(np.arange(datalen), np.ones(datalen)*340.8067, label="Partition Nearest", alpha = 0.75, linewidth = 2)
plt.plot(np.arange(datalen), np.ones(datalen)*701.6326, label="Partition Random", alpha = 0.75, linewidth = 2)

plt.ylabel("完成时间 / 秒")
plt.xlabel("训练回合")
plt.yticks([300,400,500,600,700])
plt.legend()
plt.savefig("avg_finished_time7.0.png", bbox_inches='tight', pad_inches=0.05, dpi=600)
plt.close('all')



plt.rcParams['font.sans-serif'] = 'SimSun'
plt.rcParams['font.serif'] = 'Times New Roman'
plt.rcParams['font.size'] = 12
plt.figure(figsize=(4,4))
# 生成示例数据
x = ["Partition\nRandom", "Partition\nNearest", "Nearest", "Ours"]
y1 = np.array([628.38,342.79,330.84,286.23])
error_up1 = np.array([812.82,361.65,412.49,346.62])
error_down1 = np.array([497.53,332.29,287.20,274.98])

# episode: 1550
# (286.23291900612486, 346.6276028706984, 274.9842168420126)

# 绘制误差棒图

plt.errorbar(x, y1, yerr=[y1-error_down1,error_up1-y1], fmt='ro', capsize=5)
plt.plot(x, y1, 'bo-')

plt.text(0.1, y1[0], str(y1[0]), size=10)
plt.text(1, y1[1]+25, str(y1[1]), size=10)
plt.text(2+0.05, y1[2]+25, str(y1[2]), size=10)
plt.text(3-0.2, y1[3]+20, str(y1[3]), size=10)


# 设置图表标题和坐标轴标签
# plt.title('多轮仿真实验图(15-17-18)')
plt.xlabel('算法')
plt.ylabel('完成时间 / 秒')
plt.yticks([300,400,500,600,700,800])
plt.savefig("avg_finished_time7.0_100_errorbar.png", bbox_inches='tight', pad_inches=0.05, dpi=600)
plt.close('all')