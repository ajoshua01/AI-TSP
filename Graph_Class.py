#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 23:31:12 2021

@author: aaronjoshuaesq.
"""


class Graph(object):
    
    def __init__(self, graph_dict=None, nodes = 10):
        """ initializes a graph object 
            If no dictionary or None is given, 
            an empty dictionary will be used"""
        from TSPVisualizer import Visualizer
        self.grapher = Visualizer()
        if graph_dict == None:
           self.__graph_dict = {}
           self.randomize_graph(nodes)
        self.__title = ""
        """Start pathing by calling this method first so that a starting
        location can be determined. It will output the edges of the starting 
        node. To identify the node check the location attribute"""
        import random
        self.location = ""
        self.location = random.choice(list(self.__graph_dict.keys()))
        self.grapher.add_node(self.location)  
        self.options = self.__graph_dict[self.location]
        print(self)
          

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
        for locale in self.__graph_dict.keys():
            y = 0
            while y < random.randrange(3, nodes):
                if y != x:
                    newNode = random.randrange(nodes)
                    self.__graph_dict[locale].append((newNode, locale))
                    self.__graph_dict[newNode].append((locale, locale))
                y=y+1    
        """Pop any loops from the graph"""
        for key, value in self.__graph_dict.items():
            z=0
            for edge in value:
                if key == edge[0]:
                    self.__graph_dict[key].pop(z)
                    value.pop(z)
                z=z+1
            x=x+1
        """popping duplicates"""
        for key, value in self.__graph_dict.items():
            storedEdges = set()
            z=0
            for edge in value:
                if edge[0] in storedEdges:
                    value.pop(z)
                else:
                    storedEdges.add(edge[0])
            z=z+1

    def add_edge(self, vertex, edge, weight):
        """ Assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        edge = tuple(edge)
        if vertex in self.__graph_dict.keys():

            if self.__graph_dict[vertex] == []:
               self.__graph_dict[vertex].append([edge, weight])
            else:
                if edge in self.__graph_dict[vertex]:
                    return None
                else:
                    self.__graph_dict[vertex].append([edge, weight])
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
        self.grapher.draw_graph(title = self.__title)
        return "Rendered"
    

        
    
    def path_forward(self, step):
        """The path foward takes a number (int) indicating which among the
        list of edges you wish to path to next"""
        self.grapher.add_node(self.__graph_dict[self.location][step][0])
        print("step %s" % (step))
        self.grapher.add_edge(self.location, self.__graph_dict[self.location][step][0], 
                              distance = self.__graph_dict[self.location][step][1])            
        self.__title = "Travel %s km from node %s to node %s" % (self.__graph_dict[self.location][step][1],
                                                 self.location,
                                         self.__graph_dict[self.location][step][0])
        self.location = self.__graph_dict[self.location][step][0]
        print(self)
        return self.__graph_dict[self.location]
    
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

    def print_location(self):
        if self.location == "":
            return self.__graph_dict
        else:
            return self.location
    

