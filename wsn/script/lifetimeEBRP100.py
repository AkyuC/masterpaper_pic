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

algStaticLsit = [381, 383, 375, 389, 395, 380, 382, 379, 387, 384, 389, 386, 373, 379, 396, 378, 377, 382, 380, 377, 378, 379, 369, 379, 371, 368, 383, 389, 378, 387, 370, 395, 379, 388, 381, 380, 387, 377, 373, 388, 381, 384, 379, 378, 379, 384, 374, 382, 372, 381, 381, 383, 378, 384, 386, 373, 397, 379, 392, 384, 385, 394, 382, 378, 378, 379, 371, 382, 384, 384, 370, 388, 375, 384, 386, 384, 387, 394, 371, 379, 390, 387, 390, 376, 383, 381, 385, 383, 384, 390, 385, 372, 377, 390, 384, 385, 386, 378, 392, 377]
algRandomList = [1688, 1377, 1444, 1577, 1577, 1516, 1615, 1539, 1627, 1675, 1608, 1542, 1623, 1644, 1575, 1520, 1329, 1587, 1593, 1511, 1571, 1522, 1697, 1513, 1589, 1644, 1439, 1734, 1622, 1579, 1458, 1416, 1589, 1558, 1611, 1533, 1669, 1715, 1733, 1590, 1575, 1674, 1665, 1619, 1609, 1518, 1529, 1704, 1547, 1678, 1614, 1485, 1714, 1627, 1543, 1556, 1682, 1404, 1478, 1529, 1465, 1661, 1414, 1612, 1432, 1533, 1539, 1520, 1634, 1629, 1677, 1604, 1509, 1698, 1608, 1629, 1547, 1499, 1607, 1464, 1550, 1639, 1677, 1679, 1586, 1593, 1587, 1489, 1473, 1495, 1618, 1574, 1476, 1549, 1539, 1595, 1541, 1548, 1489, 1613]
algGreedy1List = [2187, 2168, 2169, 2179, 2179, 2209, 2189, 2169, 2158, 2169, 2188, 2207, 2168, 2167, 2179, 2179, 2209, 2169, 2189, 2178, 2189, 2188, 2158, 2177, 2189, 2189, 2159, 2179, 2178, 2169, 2159, 2169, 2179, 2197, 2179, 2199, 2169, 2149, 2178, 2199, 2189, 2179, 2179, 2178, 2188, 2168, 2188, 2188, 2179, 2189, 2189, 2189, 2159, 2166, 2198, 2169, 2189, 2209, 2198, 2189, 2169, 2179, 2169, 2169, 2179, 2159, 2188, 2159, 2189, 2169, 2169, 2167, 2209, 2177, 2169, 2188, 2179, 2178, 2169, 2158, 2189, 2169, 2178, 2189, 2183, 2179, 2169, 2189, 2168, 2179, 2162, 2199, 2189, 2189, 2189, 2149, 2159, 2179, 2169, 2178]
algGreedy2List = [2262, 2303, 2293, 2283, 2293, 2272, 2281, 2273, 2265, 2263, 2282, 2284, 2242, 2273, 2254, 2300, 2312, 2313, 2252, 2301, 2291, 2283, 2281, 2253, 2293, 2282, 2262, 2256, 2283, 2283, 2302, 2271, 2273, 2291, 2295, 2254, 2292, 2294, 2265, 2273, 2281, 2282, 2291, 2273, 2281, 2262, 2291, 2253, 2266, 2302, 2300, 2280, 2272, 2263, 2271, 2264, 2283, 2274, 2255, 2310, 2243, 2235, 2299, 2252, 2282, 2291, 2285, 2275, 2292, 2264, 2305, 2285, 2272, 2284, 2275, 2275, 2255, 2284, 2254, 2262, 2267, 2273, 2271, 2265, 2282, 2277, 2273, 2263, 2255, 2264, 2273, 2272, 2274, 2263, 2271, 2292, 2266, 2313, 2293, 2300]
# Static 14, mean: 381.92, max: 397, min: 368
# algGreedy2List, mean: 2277.08, max: 2313, min: 2235
# Random, mean: 1572.9, max: 1734, min: 1329
# algGreedy1List, mean: 2178.87, max: 2209, min: 2149
DREDlist = [2529, 2509, 2499, 2517, 2528, 2489, 2478, 2518, 2519, 2534, 2499, 2498, 2499, 2518, 2499, 2508, 2497, 2508, 2538, 2517, 2525, 2459, 2519, 2488, 2489, 2507, 2499, 2518, 2496, 2489, 2489, 2507, 2506, 2528, 2546, 2499, 2505, 2508, 2529, 2497, 2529, 2487, 2529, 2517, 2497, 2536, 2498, 2508, 2509, 2497, 2497, 2516, 2479, 2508, 2509, 2518, 2506, 2519, 2517, 2458, 2477, 2539, 2508, 2487, 2489, 2499, 2499, 2499, 2497, 2458, 2509, 2529, 2509, 2488, 2499, 2518, 2507, 2486, 2488, 2508, 2515, 2489, 2497, 2499, 2518, 2517, 2499, 2468, 2508, 2489, 2519, 2536, 2526, 2489, 2458, 2489, 2489, 2509, 2507, 2509]
# seed:5, episode: 41290, mean max min: 2504.61, 2546, 2458

def calculate_confidence_interval(data):
    import numpy as np
    from scipy import stats
    # 计算平均值和标准差
    mean = np.mean(data)
    std = np.std(data)
    # 计算置信区间
    confidence_interval = stats.norm.interval(0.95, loc=mean, scale=std/np.sqrt(len(data)))
    return mean, std, confidence_interval

def switch(origin, target):
    mean, std, confidence_interval = calculate_confidence_interval(target)
    print(mean, std, max(origin), min(origin), confidence_interval)
    origin[0] = mean
    origin[1] = max(origin)
    origin[2] = min(origin)

switch(algStatic, algStaticLsit)
switch(algRandom, algRandomList)
switch(algGreedy1, algGreedy1List)
switch(algGreedy2, algGreedy2List)
switch(DRED, DREDlist)

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