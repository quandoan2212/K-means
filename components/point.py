import math

class Point:

    def __init__(self, name, x=None, y=None):
        self.name = name
        self.x = x
        self.y = y

    def measure_distance_to_other_point(self, other_point, measure_option):
        '''
        calculate the distance between this point from another point
        :param other_point:  must be a Point object
        :param measure_option: there are 2 ways for calculating the distance:
                                Mahattan(1) and Euclide(2)
        :return: a value indicates for the distance
        '''
        if measure_option == 1:
            d = abs(self.x - other_point.x) + abs(self.y - other_point.y)
        elif measure_option == 2:
            d = math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
        else:
            raise Exception("There is no option like that !!!")
        return d
