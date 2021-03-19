import utils
import domain.station as st


class Building:
    def __init__(self, building_name, building_type, coord):
        self.name = building_name
        self.type = building_type
        self.coord = []
        sum_x = []
        sum_y = []
        for c in coord:
            sum_x.append(c[1])
            sum_y.append(c[0])
            self.coord.append([c[1], c[0]])
        self.center = [sum(sum_x) / len(sum_x), sum(sum_y) / len(sum_y)]

    def into(self, station, distance=100):
        station_coord = utils.lonlat2meet(station.coord[0], station.coord[1])
        building_coord = utils.lonlat2meet(self.center[0], self.center[1])
        d = ((station_coord[0] - building_coord[0]) ** 2 + (station_coord[1] - building_coord[1]) ** 2) ** 0.5
        return d <= distance
