import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from graphviz import Digraph
import base64  # noqa: I201
from io import BytesIO  # noqa: I201

import re


class Graph(object):
    def __init__(self):
        self.graph = {}
        self.bridges = []

    def getGraph(self):
        return self.graph

    def getBridges(self):
        return self.bridges

    def parseGraph(self, data):
        temp = [bridge for bridge in re.sub(r'([\r\n\s]+)', '', data).split(',')]
        temp = list(set(temp))
        temp = list(filter(lambda br: len(br) == 2, [br.split('-') for br in temp]))
        for br in temp:
            self.addToGraph(br[0], br[1])

    def addToGraph(self, x1, x2):
        self.bridges.append([x1, x2])
        if x1 in self.graph.keys():
            self.graph[x1].append(x2)
        elif x1 not in self.graph.keys() and x2 in self.graph.keys():
            self.graph[x1] = [x2]
        else:
            self.graph[x1] = [x2]
            self.graph[x2] = []

        self.graph = {x: self.graph[x] for x in sorted(self.graph.keys())}
        self.bridges = [bridge for bridge in sorted(self.bridges, key=lambda x: (x[0], x[1]))]

    def calcDegree(self):
        return {x: len(self.graph[x]) for x in self.graph.keys()}

    def createAdjacencyMatrix(self):
        res = [[0 for _ in self.graph.keys()] for _ in self.graph.keys()]
        for colum, x in enumerate(self.graph.keys()):
            for row, items in enumerate(self.graph.keys()):
                if x in self.graph[items]:
                    res[row][colum] = 1
        return res

    def adjacencyMatrixToTable(self):
        temp = self.createAdjacencyMatrix()
        res = [[''] + list(self.graph.keys())] + \
              [[item] + temp[i] for i, item in enumerate(self.graph.keys())]
        return res

    def createIncidenceMatrix(self):
        res = [[0 for _ in range(sum(list(map(len, self.graph.values()))))] for _ in self.graph.keys()]
        for i in range(len(self.graph.keys())):
            for j, bridge in enumerate(self.bridges):
                if list(self.graph.keys())[i] == bridge[0]:
                    res[i][j] = 1
                elif list(self.graph.keys())[i] == bridge[1]:
                    res[i][j] = -1

        return res

    def incidenceMatrixToTable(self):
        temp = self.createIncidenceMatrix()
        res = list([[''] + ['q' + str(i + 1) for i, _ in enumerate(temp[0])]]) + \
              [[item] + temp[i] for i, item in enumerate(self.graph.keys())]
        return res

    def getPreimage(self):
        res = {x: [] for x in self.graph.keys()}
        for x in self.graph.keys():
            for items in self.graph.keys():
                if x in self.graph[items]:
                    res[x].append(items)
        return res

    def drawGraph(self, save=False):
        #
        # left = [i[0] for i in self.bridges]
        # right = [i[1] for i in self.bridges]
        # df = pd.DataFrame({'from': left, 'to': right})
        # G = nx.from_pandas_edgelist(df, 'from', 'to', create_using=nx.Graph())
        # fig = plt.figure(figsize=(8, 8))
        # nx.draw(G, with_labels=True, node_color='skyblue', node_size=1500)

        f = Digraph('graph', filename='static/fsm.gv',
                    node_attr={'color': 'lightblue2',
                               'style': 'filled', 'shape': 'circle'})
        f.attr(rankdir='A', size='1000')

        f.edges(self.bridges)
        # if save:
        #     plt.savefig('graph.png', facecolor=fig.get_facecolor())
        # fig.show()
        return f

    @staticmethod
    def graphImgToBytes(fig):
        tempfile = fig.pipe(format='png')
        encoded = base64.b64encode(tempfile).decode('utf-8')
        return encoded


# graph = Graph()
#
# graph.addToGraph('А', 'Б')
# graph.addToGraph('А', 'В')
# graph.addToGraph('Б', 'Г')
# graph.addToGraph('Б', 'Д')
# graph.addToGraph('В', 'Б')
# graph.addToGraph('В', 'Г')
# graph.addToGraph('В', 'Ж')
# graph.addToGraph('В', 'Е')
# graph.addToGraph('Г', 'Д')
# graph.addToGraph('Г', 'Ж')
# graph.addToGraph('Д', 'Ж')
# graph.addToGraph('Е', 'Ж')
# #
#
# graph.adjacencyMatrixToTable()
# graph.incidenceMatrixToTable()
#
# # graph.addToGraph(1, 2)
# # graph.addToGraph(2, 3)
# # graph.addToGraph(2, 4)
# # graph.addToGraph(3, 5)
# # graph.addToGraph(4, 6)
# # graph.addToGraph(5, 6)
# # graph.addToGraph(5, 2)
# # graph.addToGraph(6, 4)
#
#
#
# print(graph.getGraph())
#
# print()
# print(graph.getBridges())
# print()
# degree = graph.calcDegree()
#
# print(degree)
# print()
# preim = graph.getPreimage()
#
# print(preim)
# print()
# a = graph.createAdjacencyMatrix()
#
# for i in a:
#     print(i)
# print()
# for i in graph.createIncidenceMatrix():
#     print(i)
# print()
#
# a = graph.drawGraph(save=True)
#
# print(graph.graphImgToBytes(a))
#
#


# gra = Graph()
# #
# #
# #
# y= 0
# t = gra.graphImgToBytes(y)
# print(t)
# # f.view()
