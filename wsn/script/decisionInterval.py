import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = 'SimSun'
plt.rcParams['font.serif'] = 'Times New Roman'
plt.rcParams['font.size'] = 15

plt.figure(figsize=(12,4))


x = [ i+1 for i in range(20)]
y = [2611.2, 2572.8, 2555.7, 2533.3, 2542.7, 2532.5, 2537.2, 2524.1, 2502.1, 2504.5, 2495.1, 2464.1, 2458, 2437.6, 2412.8, 2408.4, 2377.6, 2376.7, 2355.6, 2353.4] 
error_up = np.array([2628, 2581, 2575, 2562, 2558, 2555, 2551, 2559, 2527, 2537, 2518, 2494, 2482, 2477, 2439, 2446, 2407, 2423, 2393, 2378] )
error_down = np.array([2602, 2565, 2528, 2491, 2529, 2500, 2505, 2479, 2447, 2479, 2463, 2434, 2416, 2405, 2368, 2350, 2328, 2321, 2315, 2314])

omegas = []
with open("omega", "r") as f:
    i = 0
    for line in f.readlines():
        i+=1
        if i%2==1:
            continue
        # print(line[1:len(line)-2].split(","))
        omegas.append(list(map(int, line[1:len(line)-2].split(","))))

def calculate_confidence_interval(data):
    import numpy as np
    from scipy import stats
    # 计算平均值和标准差
    mean = np.mean(data)
    std = np.std(data)
    # 计算置信区间
    confidence_interval = stats.norm.interval(0.95, loc=mean, scale=std/np.sqrt(len(data)))
    return mean, std, confidence_interval

y = []
error_down = []
error_up = []
for i in range(len(omegas)):
    # print(f"omega: {i+1}")
    mean, std, confidence_interval = calculate_confidence_interval(omegas[i])
    # print(mean, std, confidence_interval)
    y.append(int(mean))
    error_up.append(max(omegas[i]))
    error_down.append(min(omegas[i]))
    print(f"{i+1} & {int(mean)} & {float('%.2f' % std)} & {max(omegas[i])} & {min(omegas[i])} & [{float('%.2f' % confidence_interval[0])}, {float('%.2f' % confidence_interval[1])}] \\\\ \n\\hline")

y = np.array(y)
error_up = np.array(error_up)
error_down = np.array(error_down)

for i in range(len(x)):
    plt.text(i+1, int(y[i])+20, str(int(y[i])))

# 绘制误差棒图
plt.errorbar(x, y, yerr=[y-error_down,error_up-y], fmt='ro', capsize=5)
plt.plot(x, y, 'bo-')

plt.xticks(x,x)
plt.yticks([2250,2300,2350,2400,2450,2500,2550,2600,2650])

# 设置图表标题和坐标轴标签
plt.xlabel('决策间隔 / 轮')
plt.ylabel('存活时间 / 轮')

# 显示图形
plt.savefig("decisioninterval.png", bbox_inches='tight', pad_inches=0.05, dpi=600)