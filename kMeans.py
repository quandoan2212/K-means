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
        converge_time = 0
        while True:
            converge_time += 1
            list_point_distance = self.__measure_distance_to_centr()

            if converge_time == 1:
                self.centr_subset = self.__grouping_points(list_point_distance)
                self.__calc_average(self.centr_subset)
                continue

            # compare centroids' subsets, if there is no changes, break loop.
            if self.__grouping_points(list_point_distance) == self.centr_subset:
                return [converge_time, self.centr_subset, self.list_centr]
            else:
                self.centr_subset = self.__grouping_points(list_point_distance)
                self.__calc_average(self.centr_subset)
                continue



    def __measure_distance_to_centr(self):
        result = list()
        #Calculate the matrix contains distance values of all point in list to centroid points in the list
        point_distance = list()
        for p in self.list_points:
            point_distance.clear()
            for centr in self.list_centr:
                distance = p.measure_distance_to_other_point(centr, self.measure_type)
                point_distance.append(distance)
            result.append(point_distance.copy())
        return result

    def __grouping_points(self, list_distance):
        result = list()
        subset = dict()
        for centr in self.list_centr:
            subset.clear()
            subset["name"] = centr.name
            subset["points"] = list()
            position = self.list_centr.index(centr)
            for p in list_distance:
                if p.index(min(p)) == position:
                    subset["points"].append(list_distance.index(p))
            result.append(subset.copy())
        return result


    def __calc_average(self, list_centr_subset):
        self.list_centr.clear()
        for subset in list_centr_subset:
            x = mean([self.list_points[x].x for x in subset["points"]])
            y = mean([self.list_points[x].y for x in subset["points"]])
            new_centr = Point(name=subset["name"], x=x, y=y)
            self.list_centr.append(new_centr)





