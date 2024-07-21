class Vertex:
    def __init__(self, name):
        self.__links = []
        self.__vertex = []
        self.name = name  # убрать name

    def __str__(self):
        return f'{self.name}'

    @property
    def links(self):
        return self.__links

    @property
    def vertex(self):
        return self.__vertex

    @vertex.setter
    def vertex(self, n):
        self.__vertex.append(n)


class Link:
    def __init__(self, v1, v2):
        if not isinstance((v1 and v2), Vertex): raise AttributeError('указан неверный объект')
        if v2 not in v1.vertex:
            self.__v1 = v1
            self.__v1.links.append(self)
            self.__v1.vertex.append(v2)
            self.__v2 = v2
            self.__v2.links.append(self)
            self.__v2.vertex.append(v1)
            self.__dist = 1
        else:
            raise AttributeError('у этих вершин свзязь уже есть')

    @property
    def v1(self):
        return self.__v1

    @property
    def v2(self):
        return self.__v2

    @property
    def dist(self):
        return self.__dist

    @dist.setter
    def dist(self, val):
        if val <= 0: raise ValueError('длина должна быть положительной')
        self.__dist = val


class LinkedGraph:
    def __init__(self):
        self._links = []
        self._vertex = []

    def _dist_path(self, links):
        return sum([x.dist for x in links])

    def _next(self, current, link_prev, current_path, current_links):
        current_path += [current]
        if link_prev: current_links += [link_prev]

        if current == self.stop_v: return current_path, current_links

        len_path = -1
        best_path = []
        best_links = []

        for link in current.links:
            path = []
            links = []

            if link.v1 not in current_path:
                path, links = self._next(link.v1, link, current_path[:], current_links[:])
            elif link.v2 not in current_path:
                path, links = self._next(link.v2, link, current_path[:], current_links[:])

            if self.stop_v in path and (len_path > self._dist_path(links) or len_path == -1):
                len_path = self._dist_path(links)
                best_path = path[:]
                best_links = links[:]
        return best_path, best_links

    def add_vertex(self, v):
        if not isinstance(v, Vertex): raise AttributeError('указан неверный объект')
        if v not in self._vertex: self._vertex.append(v)

    def add_link(self, link):
        if not isinstance(link, Link): raise AttributeError('указан неверный объект')
        if link not in self._links: self._links.append(link)
        if link.v1 not in self._vertex: self._vertex.append(link.v1)
        if link.v2 not in self._vertex: self._vertex.append(link.v2)

    def find_path(self, start_v, stop_v):
        if (not isinstance((stop_v and start_v), Vertex) or
                (stop_v or start_v) not in self._vertex): raise AttributeError('указан неверный объект')
        self.start_v = start_v
        self.stop_v = stop_v
        return self._next(self.start_v, None, [], [])


class Station(Vertex):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'


class LinkMetro(Link):
    def __init__(self, v1, v2, dist):
        if dist <= 0 or not isinstance(dist, (int or float)): raise ValueError('длина должна быть положительной')
        super().__init__(v1, v2)
        self._dist = dist


map_graph = LinkedGraph()
v1 = Vertex('v1')
v2 = Vertex('v2')
v3 = Vertex('v3')
v4 = Vertex('v4')
v5 = Vertex('v5')
v6 = Vertex('v6')
v7 = Vertex('v7')
print(v1, v2, v3, v4, v5, v6, v7)

map_graph.add_link(Link(v1, v2))
map_graph.add_link(Link(v2, v3))
map_graph.add_link(Link(v1, v3))

map_graph.add_link(Link(v4, v5))
map_graph.add_link(Link(v6, v7))

map_graph.add_link(Link(v2, v7))
map_graph.add_link(Link(v3, v4))
map_graph.add_link(Link(v5, v6))

# print(len(map_graph._links))  # 8 связей
# print(len(map_graph._vertex))  # 7 вершин
path = map_graph.find_path(v1, v6)
print(path)
# print(v1, v1.vertex)
# print(v6, v6.vertex)

s = Station('egor')
s1 = Station('sidorov')
k = LinkMetro(s, s1, 10)
