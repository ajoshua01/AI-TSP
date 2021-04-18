#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 16:50:11 2021

@author: aaronjoshuaesq.
"""


class Visualizer:
    
    """Initilizer takes no arguments and 
    creates a new visualization object 
    using networkx library"""
     
    
    def __init__(self):
        import networkx as nx
        import matplotlib.pyplot as plt
        self.chart = nx.Graph()
        self.__fig = plt.figure(1)
        self.__numRows = 1
        print("Visualizer created")
    
    def add_node(self, node):
        """Takes an integer representing the new node to be created"""
        self.chart.add_node(node)
                
    def add_edge(self, source, destination, distance):
        """Takes three argments, source_node, destination_node, and
        distance to new node (weight)"""
        self.chart.add_edge(source,destination, weight = distance, 
                            label = destination)
        
    def draw_graph(self, graph = None, title = ""):
            import networkx as nx
            pos = nx.spring_layout(self.chart)
            # nodes
            import matplotlib.pyplot as plt
         
            self.__fig.subplots(self.__numRows, 1, 'none')
            nx.draw_networkx_labels(self.chart, pos)
            nx.draw_networkx_edges(self.chart, pos)
            nx.draw_networkx_nodes(self.chart, pos)
            print(title)           
            self.__numRows = self.__numRows + 1
            plt.axis("off")
            plt.title = title
            plt.show()
         