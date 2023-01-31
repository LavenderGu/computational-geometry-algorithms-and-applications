"""
点和线段用列表表示，例如：
点：[4,7]
线段：[[4,7],[1,3]
"""
from handle import intersection
from helper import *
import random
import matplotlib.pyplot as plt
N = 20             # 随机生成线段的数量
MAX = 1000          # 生成线段的点的坐标最大值


def scale(i):
    return float(i)

S = []          # 线段集
for i in range(N):
    p1 = (scale(random.randint(0, MAX)), scale(random.randint(0, MAX)))
    p2 = (scale(random.randint(0, MAX)), scale(random.randint(0, MAX)))
    s = (p1, p2)
    k = get_slope(s)
    if not (k == 0 or k is None):     # 暂未考虑水平线和竖直线
        plt.plot((p1[0], p2[0]),(p1[1], p2[1]))
        S.append(s)
inter = intersection(S)    #    交点
print(inter)
interps = inter.keys()

for p in interps:
    plt.scatter(p[0],p[1])

print("NED")
plt.show()
