from components.point import Point
class KMeans:

    def __init__(self, K, measure_type, list_points, first_centr, second_centr):
        self.K = K
        self.measure_type = measure_type
        self.list_points = list_points
        self.first_centr = first_centr
        self.second_centr = second_centr

    def measure_distance_to_centr(self):
        result = []
        for p in self.list_points:
            d_one = p.measure_distance_to_other_point(self.first_centr)
            d_two = p.measure_distance_to_other_point(self.second_centr)
            distance_point = Point(format("%s to centroid", p.name), d_one, d_two)
            result.append(distance_point)
        return result

