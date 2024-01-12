import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = 'SimSun'
plt.rcParams['font.serif'] = 'Times New Roman'
plt.rcParams['font.size'] = 15

plt.figure(figsize=(10,3))

avg_finished_time = np.loadtxt("avg_finished_time7.0")
avg_finished_time_without_GAE = np.loadtxt("avg_finished_time7.1")

datalen = 2010 if len(avg_finished_time) > 2010 else len(avg_finished_time)

plt.plot(np.arange(datalen), avg_finished_time[:datalen], label="Ours", linewidth = 2)
plt.plot(np.arange(datalen), avg_finished_time_without_GAE[:datalen], label="Ours Without Duration", linewidth = 2, alpha = 0.75)


plt.ylabel("完成时间 / 秒")
plt.xlabel("训练回合")
plt.yticks([300,400,500,600,700])
plt.legend()
plt.savefig("GAE_compared.png", bbox_inches='tight', pad_inches=0.05, dpi=600)
plt.close('all')