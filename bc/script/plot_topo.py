import matplotlib.pyplot as plt
import numpy as np

def plot_topo(locs):
    plt.rcParams['font.sans-serif'] = 'SimSun'
    plt.rcParams['font.serif'] = 'Times New Roman'
    plt.rcParams['font.size'] = 11
    plt.figure(figsize=(8, 8))
    plt.rcParams['axes.unicode_minus'] = False

    pos_node = []
    x = []
    y = []
    x_bs = np.array([100,-100,100,-100])
    y_bs = np.array([100,100,-100,-100])
    plt.scatter(x_bs, y_bs, s=21**2, color='r', facecolors='none', marker='s', linewidth=1.2)
    for i in range(len(x_bs)):
        plt.text(x_bs[i]-4, y_bs[i]-2, 'CS'+str(i))
    for i,(xi,yi) in enumerate(locs):
        x.append(xi)
        y.append(yi)
        if i < 9:
            plt.text(xi-1.5, yi-2, str(i+1))
        else:
            plt.text(xi-2.5, yi-2, str(i+1))
    plt.scatter(x, y, s=15**2, color='black', facecolors='none', linewidth=1.2)
    plt.xlim((-110,110))
    plt.ylim((-110,110))
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.savefig("topo.png", bbox_inches='tight', pad_inches=0.05, dpi=600)
    return pos_node

locs = [(-70, -56), (-30, 14), (-70, 42), (5, -27), (60, -26), 
            (8, 25), (59, 4), (24, 44), (-33, 34), (29, -88), 
            (42, 79), (-14, -27), (62, 65), (-89, -67), (93, 55), 
            (-90, 53), (-53, -28), (2, -74), (51, 20), (92, -57), 
            (19, -69), (-64, 3), (-91, -6), (79, -25), (-95, 25), 
            (-84, 32), (-78, 10), (34, -21), (7, -17), (-5, -88), 
            (3, 59), (-21, 69), (-32, 49), (-62, -71), (-18, -19), 
            (-4, 24), (20, -86), (-6, -17), (-27, -25), (34, -10), 
            (-51, 63), (41, 18), (-49, -20), (-8, -33), (32, 72), 
            (0, 9), (-32, 3), (54, 94), (-34, 74), (-33, 63)]
plot_topo(locs)