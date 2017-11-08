from vertex import Vertex
import sys


class Graph:
    def __init__(self):
        self.vertices = []
        self.n = 0

    # SETTING the mark to False in every Vertex
    def unCheckAll(self):
        for i in self.vertices:
            i.mark = False

    def addVertex(self, name):
        vert = Vertex(name)
        self.vertices.append(vert)
        self.n += 1
        return vert

    # We search the vertex 'v' in the list of Vertex so we can know if it is a valid vertex
    def isValidVertex(self, v):
        i = 0
        while i < len(self.vertices):
            if v == self.vertices[i].name:
                return True
            i += 1
        return False

    # Select the vertex 'v' in the list of Vertex, cuz the 'v' is a String and
    # we need the vertex with the name of 'v'
    def findVertex(self, v):
        i = 0
        while i < len(self.vertices):
            if v == self.vertices[i].name:
                return self.vertices[i]
            i += 1
        return None

    def dfs1(self, v):
        print(" " + v)
        x = self.findVertex(v)
        x.mark = True
        i = 0
        while i < len(x.links):
            w = x.links[i][0]
            z = self.findVertex(w)
            if z.mark is False:
                self.dfs1(z.name)
            i += 1

    def dfs(self, v):
        if not self.isValidVertex(v):
            print('Error::dfs-vertex is not Valid')
        self.unCheckAll()
        print ('DFS: ')
        self.dfs1(v)

    def bfs(self, v):
        if not self.isValidVertex(v):
            print('Error::bfs-vertex is not Valid')
        self.unCheckAll()
        queue = [v]
        x = self.findVertex(v)
        x.mark = True
        print ('BFS:')
        while len(queue) != 0:
            w = queue.pop()
            z = self.findVertex(w)
            print (" " + z.name)
            i = 0
            while i < len(z.links):
                m = z.links[i][0]
                n = self.findVertex(m)
                i += 1
                if n.mark is False:
                    queue.append(n.name)
                    n.mark = True

    # We need to check if there is a way from 'vo' to 'vf' before we start to use the Graph
    # vo = Initial Vertex
    # vf = Destiny Vertex
    def awayfrom(self, vo, vf):
        self.dfs(vo)
        x = self.findVertex(vf)
        return x.mark

    # cost between two vertex, 'vf' must be in the adjacency list of the vertex 'vo'
    def cost(self, vo, vf):
        x = self.findVertex(vo)
        i = 0
        while i < len(x.links):
            z = x.links[i][0]
            if vf == z:
                return x.links[i][1]
            i += 1

        return 0

    # Dijkstra Algorythm

    def Dijkstra(self, vo, vf):
        if not self.awayfrom(vo, vf):
            print('Error::Shortest Path: ' + vo + ' --> ' + vf)

        else:
            self.unCheckAll()
            x = self.shortestPath(vo, vf)
            return x

    def shortestPath(self, vo, vf):
        x = self.findVertex(vo)
        if not x.mark:
            x.mark = True
            m = sys.maxsize
            i = 0
            while i < len(x.links):

                if x.links[i][0] == vf:
                    m = self.cost(vo, vf)
                else:
                    data = self.shortestPath(x.links[i][0], vf)
                    newData = self.cost(vo, x.links[i][0])
                    if (data + newData) < m:
                        m = data + newData
                i += 1
                self.unCheckAll()
            if m == sys.maxsize:
                return 0
            else:
                return m

        return 0
