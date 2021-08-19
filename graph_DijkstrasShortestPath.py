import sys


class Graph():
    VERTICES = 0

    INVALID_VERTEX = -1
    INF = sys.maxsize

    known_condition = []
    min_costs = []
    previous_vertex = []

    graph = [[]]

    def __init__(self, _VERTICES, _graph):
        self.VERTICES = _VERTICES
        self.graph = _graph

        for i in range(0, self.VERTICES):
            self.known_condition.append(0)
            self.min_costs.append(sys.maxsize)
            self.previous_vertex.append(self.INVALID_VERTEX)

    def findSmallestUnknown(self):
        min_cost = self.INF
        min_cost_vertex = self.INVALID_VERTEX

        for i in range(0, self.VERTICES):
            if self.known_condition[i] == 0:
                if self.min_costs[i] < min_cost:
                    min_cost = self.min_costs[i]
                    min_cost_vertex = i

        return min_cost_vertex

    def DijkstrasShortestPath(self, start_vertex):
        self.min_costs[start_vertex] = 0

        while True:
            min_cost_vertex = self.findSmallestUnknown()
            if min_cost_vertex == self.INVALID_VERTEX:
                break
            self.known_condition[min_cost_vertex] = 1

            for i in range(0, self.VERTICES):
                if self.graph[min_cost_vertex][i] != self.INF and self.known_condition[i] == 0:
                    cost = self.graph[min_cost_vertex][i]
                    if self.min_costs[min_cost_vertex] + cost < self.min_costs[i]:
                        self.min_costs[i] = self.min_costs[min_cost_vertex] + cost
                        self.previous_vertex[i] = min_cost_vertex

    # def PrintPath(self, vertex):
    #     if self.INVALID_VERTEX != vertex:
    #         self.PrintPath(self.previous_vertex[vertex])
    #         print(' ' + str(vertex + 1))

    def getPath(self, vertex):
        path = []

        while self.INVALID_VERTEX != vertex:
            path.append(vertex)
            vertex = self.previous_vertex[vertex]

        return path
