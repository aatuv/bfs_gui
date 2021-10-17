from collections import defaultdict

class Graph:

    def __init__(self, connections=[]):
        self.__graph = defaultdict(set)
        self.add_connections(connections)

    def add_connections(self, connections):
        for node1, node2 in connections:
            self.add(node1, node2)
    
    def add(self, node1, node2):
        self.__graph[node1].add(node2)
        self.__graph[node2].add(node1)
    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.__graph))