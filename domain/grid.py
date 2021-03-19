class Grid:
    def __init__(self, location):
        self.value = 0
        self.gid = ""
        self.coord = []
        for c in location:
            self.coord.append([c[1], c[0]])

    def into(self, station):
        if self.coord[0][0] <= station.coord[0] <= self.coord[2][0]:
            if self.coord[0][1] <= station.coord[1] <= self.coord[2][1]:
                return True
        return False

    def __str__(self):
        return "gid : {}, size : {}, coord : {}".format(self.gid, self.value, self.coord[0])
