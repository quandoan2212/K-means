from components.point import Point
from numpy import mean

class KMeans:

    def __init__(self, K, measure_type, list_points, list_centr):
        self.K = K
        self.measure_type = measure_type
        self.list_points = list_points
        if len(list_centr) == K:
            self.list_centr = list_centr
        else:
            raise Exception("==== Number of initial centroids must equal to K value ====")

    def solveKmeans(self):
        pass

    def measure_distance_to_centr(self):
        result = list()

        #Calculate the matrix contains distance values of all point in list to centroid points in the list
        point_distance = list()
        for p in self.list_points:
            point_distance.clear()
            for centr in self.list_centr:
                distance = p.measure_distance_to_other_point(centr, self.measure_type)
                point_distance.append(distance)
            result.append(point_distance)
        return result

    def grouping_points(self, list_distance):
        result = list()
        subset = dict()
        for centr in self.list_centr:
            subset.clear()
            subset["name"] = centr.name
            subset["points"] = list()
            position = self.list_centr.index(centr)
            for p in list_distance:
                if p.index(min(p)) == position:
                    subset["points"].append(p)
                    list_distance.remove(p)
            result.append(subset)
        return result


    def calc_average(self):
        pass






