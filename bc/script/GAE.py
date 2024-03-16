import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = 'SimSun'
plt.rcParams['font.serif'] = 'Times New Roman'
plt.rcParams['font.size'] = 15

plt.figure(figsize=(10,3))

avg_finished_time = np.loadtxt("avg_finished_time7.0")
print(min(avg_finished_time))
avg_finished_time_without_GAE = np.loadtxt("avg_finished_time7.1")
print(min(avg_finished_time_without_GAE))
avg_finished_time_without_scaling = np.loadtxt("avg_finished_time7.6")

datalen = 2010 if len(avg_finished_time) > 2010 else len(avg_finished_time)

plt.plot(np.arange(datalen), avg_finished_time[:datalen], label="Ours", linewidth = 2)
plt.plot(np.arange(datalen), avg_finished_time_without_GAE[:datalen], label="Ours Without Duration", linewidth = 2, alpha = 0.75)
plt.plot(np.arange(datalen), avg_finished_time_without_scaling[:datalen], label="Ours Without Scaling", linewidth = 2, alpha = 0.75)


plt.ylabel("完成时间 / 秒")
plt.xlabel("训练回合")
# plt.yticks([300,400,500,600,700])
plt.legend()
plt.savefig("GAE_compared.png", bbox_inches='tight', pad_inches=0.05, dpi=600)
plt.close('all')

plt.figure(figsize=(10,3))

# avg_finished_time = np.loadtxt("avg_finished_time7.0")
avg_finished_time_decpomdp = np.loadtxt("avg_finished_time8.0")
datalen = 6010
plt.plot(np.arange(datalen), avg_finished_time_decpomdp[:datalen], label="DecPOMDP", linewidth = 2, alpha = 0.75)
plt.plot(np.arange(datalen), np.ones(datalen)*282.35, label="Optimal", alpha = 0.75, linewidth = 2)
plt.plot(np.arange(datalen), np.ones(datalen)*281.72, label="Ours", alpha = 0.75, linewidth = 2)
plt.plot(np.arange(datalen), np.ones(datalen)*362.6101, label="Nearest", alpha = 0.75, linewidth = 2)
plt.plot(np.arange(datalen), np.ones(datalen)*340.8067, label="Partition Nearest", alpha = 0.75, linewidth = 2)
plt.plot(np.arange(datalen), np.ones(datalen)*701.6326, label="Partition Random", alpha = 0.75, linewidth = 2)


plt.ylabel("完成时间 / 秒")
plt.xlabel("训练回合")
plt.yticks([300,400,500,600,700])
plt.legend()
plt.savefig("DecPOMDP_compared.png", bbox_inches='tight', pad_inches=0.05, dpi=600)
plt.close('all')