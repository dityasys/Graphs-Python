class Vertex:
    def __init__(self, name):
        self.name = name
        self.links = []
        self.mark = False

    def addEdge(self, vd, cost):
        self.links.append([vd, cost])
