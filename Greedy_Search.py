# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 14:15:45 2021

@author: Kyle
"""
from Graph_Class import Graph

#This is the first iteration of the Greedy Algorithm. It has some issues and is missing features, but it actually does SOMETHING
#Currently, the algorithm will: 

#graph declaration
graph = Graph()

#visited nodes declaration - unused
visitedNodes = [];

#Subtracting like-values from Python is pretty weird when you're using lists. Here's a function to make it easier
def diff(first, second):
        second = set(second)
        return [item for item in first if item not in second]


#test prints to help comprehension
print("graph location: ", graph.location)

#print("All adjacent nodes to our location: ", graph.vertex(graph.location))



vertexList = graph.vertex(graph.location)
vertexInnerTuple = vertexList[0]
print("The value of the first element in the tuple[first element of the list], within the list[return value of the graph.vertex method]")
print(vertexInnerTuple[0])

#variable declarations
#I know these two variables are lists but I named them before I declared them and at this point I'm afraid to refactor anything
edgeArray = []
nodeArray = []
minValue = 20
minimumValueIndex = 0
stepCounter = 0

#stepCounter is an improper condition for the loop - it is only used to prevent race conditions while testing
#TODO: replace this condition with the proper condition
while (stepCounter < 10):
    print("Here's where we are: ", graph.location)
    print("Here's what is around us: ", graph.vertex(graph.location))
    vertexList = graph.vertex(graph.location)
    
    visitedNodes.append(graph.location)
    edgeArray.clear()
    nodeArray.clear()
    minValue = 20
    #Time to build an array of the nearby nodes so we can look at them and traverse
    #We're not interested in nodes we have history with, so we skip them.
    
    for x in vertexList:
        #print("vertex Inner Tuple value for List value ", x, ": ", x[0])
        if (x[1] in visitedNodes):
            edgeArray.append(1000) #Build an array, edgeArray, of all distances between potential nodes
            nodeArray.append(x[1]) #Build an array, nodeArray, with the 'address' of all the nearby nodes
        else: 
            edgeArray.append(x[0]) #Build an array, edgeArray, of all distances between potential nodes
            nodeArray.append(x[1]) #Build an array, nodeArray, with the 'address' of all the nearby nodes
    print("array of all edges: ", edgeArray)
    print("Node history: ", visitedNodes)
    print("Nodes we haven't visited that are adjacent: ", nodeArray)
    
    for x in range(0, len(edgeArray)):
        if(edgeArray[x] < minValue):
            minValue = edgeArray[x] #Find lowest distance node, make note of it in minimumValueIndex, then move there
            minimumValueIndex = edgeArray.index(minValue)
    print("minimum distance value in the edgeArray: ", minValue)
    print("Index value of the minimum value element: ", minimumValueIndex)
    if (minValue == 20):
        graph.path_forward(visitedNodes[-1])
    else:   
        graph.path_forward(minimumValueIndex)
    stepCounter += 1
    
#find closest node.
#if node is in list, remove it from potential addresses and search again



#Basic idea of algorithm procedure below

#While the number of addresses in the array is less than [number of nodes], do code 
# 1. look at distance to all nearby nodes
# 2. initiate move to closest node/track nodes which have been visited
# 3. when there are no acceptable nodes to move to ->
# 4. move back to previous node and follow another route.


#questions to answer: graph.vertex offers a list of tuples, what are each of the values in the tuple?
#How come there are sometimes duplicates for distance[acceptable] or possibly for node addresses[unacceptable - multiple paths to the same node??]
