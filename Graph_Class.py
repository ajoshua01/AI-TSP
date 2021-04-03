#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 23:31:12 2021

@author: aaronjoshuaesq.
"""
import random

class Graph(object):

    def __init__(self, graph_dict=None, nodes = 10):
        """ initializes a graph object 
            If no dictionary or None is given, 
            an empty dictionary will be used
        """
        if graph_dict == None:
           graph_dict = {}
           self.__graph_dict = graph_dict
           self.randomize_graph(nodes)

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph 
            not currently working.
        """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in 
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. 
            Otherwise nothing has to be done. 
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []
            
    def randomize_graph(self, nodes):
        import random
        x=0
        self.__graph_dict = {}
        while x < nodes:
            self.__graph_dict[x]  = []
            x=x+1
        x = 0
        for x in self.__graph_dict.keys():
            y = 0
            while y < random.randrange(3, nodes):
                if y != x:
                    newNode = random.randrange(nodes)
                    self.__graph_dict[x].append((newNode, x))
                    self.__graph_dict[newNode].append((x, x))
                y=y+1
    
        """Pop any loops from the graph"""
        for key, value in self.__graph_dict.items():
            z=0
            for edge in value:
                if key == edge[0]:
                    self.__graph_dict[key].pop(z)
                    value.pop(z)
                    print("popped %s" % edge[0])
                z=z+1
            x=x+1
        """popping duplicates"""
        for key, value in self.__graph_dict.items():
            storedEdges = set()
            z=0
            for edge in value:
                if edge[0] in storedEdges:
                    print("%s: %s"%(key, value))
                    print("Popping %s"%edge[0])
                    print(storedEdges)
                    value.pop(z)
                else:
                    storedEdges.add(edge[0])
            z=z+1

    def add_edge(self, vertex, edge):
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        edge = tuple(edge)
        if vertex in self.__graph_dict.keys():

            if self.__graph_dict[vertex] == []:
               self.__graph_dict[vertex].append(edge)
            else:
                if edge in self.__graph_dict[vertex]:
                    return None
                else:
                    self.__graph_dict[vertex].append(edge)
        else:
            print("%s does not exist" %vertex)
        
    def __generate_edges(self):
        """ A static method generating the edges of the 
            graph "graph". Edges are represented as sets 
            with one (a loop back to the vertex) or two 
            vertices 
        """
        edges = []
        for vertex in self.__graph_dict:
            print("Checking dictionary for vertex")
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    print(neighbour)
                    print(vertex)
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res
    
    location = ""
    def path_begin(self, start):
        self.location = start
        return self.__graph_dict[start]
    
    def path_forward(step):
        if self.location == "":
            print("Must begin the path before moving forward.")
            return None
        location = step
        return self.__graph_dict[step]
    
    def is_connected(self, 
                     vertices_encountered = None, 
                     start_vertex=None):
        """ determines if the graph is connected """
        if vertices_encountered is None:
            vertices_encountered = set()
        gdict = self.__graph_dict        
        vertices = list(gdict.keys()) # "list" necessary in Python 3 
        if not start_vertex:
            # chosse a vertex from graph as a starting point
            start_vertex = vertices[0]
        vertices_encountered.add(start_vertex)
        if len(vertices_encountered) != len(vertices):
            for vertex in gdict[start_vertex]:
                if vertex not in vertices_encountered:
                    if self.is_connected(vertices_encountered, vertex):
                        return True
        else:
            return True
        return False
    
    def find_path(self, start_vertex, end_vertex, path=None):
        """ find a path from start_vertex to end_vertex 
            in graph """
        if path == None:
            path = []
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex, 
                                               end_vertex, 
                                               path)
                if extended_path: 
                    return extended_path
        return None
    
    def print(self):
        print(self.__graph_dict)
    

