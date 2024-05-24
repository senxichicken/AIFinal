'''複製，使用ChatGPT推薦方式並解答'''

from random import randint, random
import math

citys = [
    (0,3),(0,0),
    (0,2),(0,1),
    (1,0),(1,3),
    (2,0),(2,3),
    (3,0),(3,3),
    (3,1),(3,2)
]

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def pathLength(p):
    dist = 0
    plen = len(p)
    for i in range(plen):
        dist += distance(citys[p[i]], citys[p[(i+1)%plen]])
    return dist

def get_neighbor_path(path):
    neighbor_path = path[:]
    i = randint(0, len(path) - 1)
    j = randint(0, len(path) - 1)
    neighbor_path[i], neighbor_path[j] = neighbor_path[j], neighbor_path[i]
    return neighbor_path

def simulated_annealing(citys, initial_temp, cooling_rate, max_iter):
    current_path = [i for i in range(len(citys))]
    current_length = pathLength(current_path)
    best_path = current_path
    best_length = current_length
    temp = initial_temp

    for _ in range(max_iter):
        neighbor_path = get_neighbor_path(current_path)
        neighbor_length = pathLength(neighbor_path)
        delta = neighbor_length - current_length

        if delta < 0 or random() < math.exp(-delta / temp):
            current_path = neighbor_path
            current_length = neighbor_length

            if current_length < best_length:
                best_path = current_path
                best_length = current_length

        temp *= cooling_rate

    return best_path, best_length

best_path, best_length = simulated_annealing(citys, initial_temp=100, cooling_rate=0.95, max_iter=10000)
print("Best Path:", best_path)
print("Best Length:", best_length)

'''
輸出
Best Path: [4, 6, 8, 10, 11, 9, 7, 5, 0, 2, 3, 1]
Best Length: 12.0
'''