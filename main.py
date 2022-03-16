from components.point import Point
from kMeans import KMeans

problem = KMeans(K=2, measure_type=2, list_centr=[Point("C1", 1, 1), Point("C2", 2, 1)],
                 list_points=[Point("A", 1, 1), Point("B", 2, 1),
                              Point("C", 4, 3), Point("D", 5, 4)])

# problem = KMeans(K=2, measure_type=2, list_centr=[Point("C1", 3, 2), Point("C2", 3, 1)],
#                  list_points=[Point("A", 1, 1), Point("B", 0, 2),
#                               Point("C", 2, 2), Point("D", 1, -1),
#                               Point("E", -1, -1), Point("F", 1, -2)])
result = problem.solveKmeans()
print(result)
for p in result[2]:
    print("CentrName: "+ p.name + ", x=" + str(p.x) + ", y=" + str(p.y))



print("hello")

