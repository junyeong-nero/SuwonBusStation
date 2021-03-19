class Station:
    def __init__(self, station_id, name, lon=0, lat=0):
        self.id = station_id
        self.name = name
        self.coord = [lat, lon]
        self.point = 0
        self.people_work = 0
        self.people_old = 0
        self.people_teen = 0

    def get_people_data(self):
        return "old : {}\nwork : {}\nteen : {}".format(self.people_old, self.people_work, self.people_teen)

    def __str__(self):
        return "id : {} / name : {} / coord : {} \n POINT : {}".format(
            self.id, self.name, self.coord, self.point)
