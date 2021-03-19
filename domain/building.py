import utils
import domain.station as st


class Building:
    def __init__(self, building_name, building_type, coord):
        self.name = building_name
        self.type = building_type
        self.coord = []
        for c in coord:
            self.coord.append([c[1], c[0]])

    def into(self, station, distance=100):
        station_coord = utils.lonlat2meet(station.coord[0], station.coord[1])
        building_coord = utils.lonlat2meet(self.coord[0][0], self.coord[0][1])
        d = ((station_coord[0] - building_coord[0]) ** 2 + (station_coord[1] - building_coord[1]) ** 2) ** 0.5
        print(d)
        return d <= distance
