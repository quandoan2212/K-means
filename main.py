from components.point import Point

a = Point("A", 1, 3)
b = Point("B", 2, 4)

d_a_to_b = a.measure_distance_to_other_point(b, 1)
print(d_a_to_b)




