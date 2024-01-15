import math

p = [(1, 1), (2, 2), (1, 2)]
def distancy(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
def pair(p):
    min_distance = float('inf')
    closest = None
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            dist = distancy(p[i], p[j])
            if dist < min_distance:
                min_distance = dist
                closest = (p[i], p[j])
    return closest

print("Ближайшая пара точек:", pair(p))
