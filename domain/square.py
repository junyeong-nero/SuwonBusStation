class Square:
    def __init__(self, location):
        self.size = 0
        self.gid = ""
        self.coord = []
        for c in location:
            self.coord.append([c[1], c[0]])



    def __str__(self):
        return "gid : {}, size : {}, coord : {}".format(self.gid, self.size, self.coord[0])


