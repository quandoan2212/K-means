from components.point import Point
# from operator import eq
#
# a = Point("A", 1, 3)
# b = Point("B", 2, 4)
#
# d_a_to_b = a.measure_distance_to_other_point(b, 1)
# print(d_a_to_b)
# import numpy
#
# list_temp = [1, 2, 3]
# res = numpy.mean([x for x in list_temp])
# print(res)


# b = {
#     "name": "A1",
#     "points": [0]
# }
# c = {
#     "name": "A2",
#     "points": [1, 2, 3]
# }
# a = [b, c]
#
# d = {
#     "name": "A1",
#     "points": [0]
# }
# e = {
#     "name": "A2",
#     "points": [1, 2, 3]
# }
# f = [d, e]
# print(a == f)

from kMeans import KMeans
problem = KMeans(K=2, measure_type=2, list_centr=[Point("C1", 1, 1), Point("C2", 2, 1)],
                 list_points=[Point("A", 1, 1), Point("B", 2, 1),
                              Point("C", 4, 3), Point("D", 5, 4)])
result = problem.solveKmeans()
print(result)
for p in result[2]:
    print("CentrName: "+ p.name + ", x=" + str(p.x) + ", y=" + str(p.y))

