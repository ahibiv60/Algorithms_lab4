from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.docs = []
        self.v = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v] = self.graph[v]

    def visit_document(self, v, visited, sort_list):
        visited[v] = True
        for neighbour in self.graph[v]:
            if not visited[neighbour]:
                self.visit_document(neighbour, visited, sort_list)
        sort_list.append(v)

    def find_order(self):
        if self.is_cyclic():
            return print("graph has a cycle")

        visited = {vertex: False for vertex in self.graph}
        sort_list = []

        for v in self.graph:
            if not visited[v]:
                self.visit_document(v, visited, sort_list)

        return sort_list

    def is_cyclic(self):
        visited = [False] * self.v
        rec_stack = [False] * self.v

        for node in self.docs:
            if not visited[self.docs.index(node)]:
                if self.is_cyclic_util(node, visited, rec_stack):
                    return True

        return False

    def is_cyclic_util(self, v, visited, rec_stack):
        visited[self.docs.index(v)] = True
        rec_stack[self.docs.index(v)] = True

        for neighbour in self.graph[v]:
            if not visited[self.docs.index(neighbour)]:
                if self.is_cyclic_util(neighbour, visited, rec_stack):
                    return True
            elif rec_stack[neighbour]:
                return True
        rec_stack[v] = False
        return False


graph = Graph(8)
data = open("govern.in", "r")
contents = data.readlines()

for document in contents:
    res = [i for i in document.split()]
    graph.add_edge(res[0], res[1])

f = open("govern.out", "w+")
for item in graph.find_order():
    f.write(item + "\n")

f.close()
