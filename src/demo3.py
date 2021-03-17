class Vert:
    def __init__(self, value):
        self.value = value
        self.connections = {}

    def __str__(self):
        return f'{self.value} connections: {str([x.value for x in self.connections])}'

    def add_edge(self, vert, weight):
        self.connections[vert] = weight

class Graph:
    def __init__(self):
        # Use a dict to represent the vertices in this graph -- adjacency list
        self.vertices = {}
        self.count = 0

    def add_vert(self, value):
        new_vert = Vert(value)

        self.vertices[value] = new_vert
        self.count += 1

        return self.vertices[value]

    def add_edge(self, vert1, vert2, weight=1):
        if vert1 not in self.vertices:
            self.add_vert(vert1)

        if vert2 not in self.vertices:
            self.add_vert(vert2)

        self.vertices[vert1].add_edge(self.vertices[vert2], weight)

    def get_vertices(self):
        return self.vertices.keys()

    def get_edges(self):
        return [x.__str__() for x in self.vertices.items()]

    def get_paths_helper(self, vert, paths, currPath):
        currPath.append(vert.value)
        neighbors = vert.connections

        for neighbor in neighbors:
            self.get_paths_helper(neighbor, paths, currPath.copy())

        # Base Case -- no neighbors
        if len(neighbors) == 0:
            paths.append(currPath)

        return paths

    def get_paths(self, key, paths=[]):
        vert = self.vertices[key]

        self.get_paths_helper(vert, paths, [])
        paths = sorted(paths)

        return paths


graph = Graph()

graph.add_vert('A')
graph.add_vert('B')

graph.add_vert('C')
graph.add_vert('D')
graph.add_vert('E')

graph.add_edge('A', 'B')

graph.add_edge('B', 'C')
graph.add_edge('C', 'D')
graph.add_edge('C', 'E')

# print(graph.get_vertices())
# print(graph.get_edges())

print(graph.get_paths('A'))

