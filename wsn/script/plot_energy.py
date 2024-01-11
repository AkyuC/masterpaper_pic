import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = 'SimSun'
plt.rcParams['font.serif'] = 'Times New Roman'
plt.rcParams['font.size'] = 15

plt.figure(figsize=(10,4))

DRED = np.loadtxt("energy_data/DRED_total_energy")/0.15*100/20
print(DRED[-1])
Greedy1 = np.loadtxt("energy_data/MaxEnergy_total_energy")/0.15*100/20
Greedy2 = np.loadtxt("energy_data/Greedy_total_energy")/0.15*100/20
Random = np.loadtxt("energy_data/Random_total_energy")/0.15*100/20
Static = np.loadtxt("energy_data/Static_n12_total_energy")/0.15*100/20

plt.plot(np.linspace(10, len(DRED)*10, len(DRED)), DRED, label="DRED")
plt.plot(np.linspace(10, len(Greedy1)*10, len(Greedy1)), Greedy1, label='Greedy1')
plt.plot(np.linspace(10, len(Greedy2)*10, len(Greedy2)), Greedy2, label='Greedy2')
plt.plot(np.linspace(10, len(Random)*10, len(Random)), Random, label='Random')
plt.plot(np.linspace(10, len(Static)*10, len(Static)), Static, label='Static')


plt.xlabel('存活时间 / 轮')
plt.ylabel('网络剩余的能量 / 百分比')
plt.legend()

plt.savefig("total_energy.png", bbox_inches='tight', pad_inches=0.05, dpi=600)
plt.cla()


DRED = np.loadtxt("energy_data/DRED_total_energy_consumed")
Greedy1 = np.loadtxt("energy_data/MaxEnergy_total_energy_consumed")
Greedy2 = np.loadtxt("energy_data/Greedy_total_energy_consumed")
Random = np.loadtxt("energy_data/Random_total_energy_consumed")
Static = np.loadtxt("energy_data/Static_n12_total_energy_consumed")

plt.plot(np.linspace(10, len(DRED)*10, len(DRED)), DRED, label="DRED")
plt.plot(np.linspace(10, len(Greedy1)*10, len(Greedy1)), Greedy1, label='Greedy1')
plt.plot(np.linspace(10, len(Greedy2)*10, len(Greedy2)), Greedy2, label='Greedy2')
plt.plot(np.linspace(10, len(Random)*10, len(Random)), Random, label='Random')
plt.plot(np.linspace(10, len(Static)*10, len(Static)), Static, label='Static')


plt.xlabel('存活时间 / 轮')
plt.ylabel('网络消耗的能量 / 焦耳')
plt.legend()

plt.savefig("total_energy_consumed.png", bbox_inches='tight', pad_inches=0.05, dpi=600)
plt.cla()


DRED = np.loadtxt("energy_data/DRED_node_energy_range")/0.15*100
print(DRED[-1])
Greedy1 = np.loadtxt("energy_data/MaxEnergy_node_energy_range")/0.15*100
Greedy2 = np.loadtxt("energy_data/Greedy_node_energy_range")/0.15*100
Random = np.loadtxt("energy_data/Random_node_energy_range")/0.15*100
Static = np.loadtxt("energy_data/Static_n12_energy_range")/0.15*100

colors =['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

plt.plot(np.linspace(10, len(DRED)*10, len(DRED)), DRED[:,0], label="DRED", color=colors[0])
plt.fill_between(np.linspace(10, len(DRED)*10, len(DRED)), DRED[:,2], DRED[:,1], color=colors[0], alpha=0.3, edgecolor='none')

plt.plot(np.linspace(10, len(Greedy1)*10, len(Greedy1)), Greedy1[:,0], label='Greedy1', color=colors[1])
plt.fill_between(np.linspace(10, len(Greedy1)*10, len(Greedy1)), Greedy1[:,2], Greedy1[:,1], color=colors[1], alpha=0.3, edgecolor='none')

plt.plot(np.linspace(10, len(Greedy2)*10, len(Greedy2)), Greedy2[:,0], label='Greedy2', color=colors[2])
plt.fill_between(np.linspace(10, len(Greedy2)*10, len(Greedy2)), Greedy2[:,2], Greedy2[:,1], color=colors[2], alpha=0.3, edgecolor='none')

plt.plot(np.linspace(10, len(Random)*10, len(Random)), Random[:,0], label='Random', color=colors[3])
plt.fill_between(np.linspace(10, len(Random)*10, len(Random)), Random[:,2], Random[:,1], color=colors[3], alpha=0.3, edgecolor='none')

plt.plot(np.linspace(10, len(Static)*10, len(Static)), Static[:,0], label='Static', color=colors[4])
plt.fill_between(np.linspace(10, len(Static)*10, len(Static)), Static[:,2], Static[:,1], color=colors[4], alpha=0.3, edgecolor='none')


plt.xlabel('存活时间 / 轮')
plt.ylabel('节点剩余能量 / 百分比')
plt.legend()

plt.savefig("node_energy_range.png", bbox_inches='tight', pad_inches=0.05, dpi=600)
plt.cla()


countEnd = []
for i in range(20):
    DRED = np.loadtxt(f"energy_data/DRED_node{i}_energy")/0.15*100
    countEnd.append(DRED[-1])
print(countEnd)

DRED_died = np.array([0.0033675333020001673, 0.0040385339899994465, 0.0008906902590000729, 0.004415023960999743, 0.004327634480000042, 0.0022826615479999914, 0.003334505723000799, 0.003714366422000659, 0.0053679856590001475, 0.0038430728549998967, 0.004873974379000091, 0.003601975363000291, 0.0056789042750001635, 0.004442037088999687, 0.004959119830999524, 0.0048145064980002795, 0.0027660124810002574, 0.00226219456899983, 0.004037684322999373])
print(np.mean(DRED_died)/0.15*100, max(DRED_died)/0.15*100, min(DRED_died)/0.15*100)
print(np.mean(DRED_died), max(DRED_died), min(DRED_died))