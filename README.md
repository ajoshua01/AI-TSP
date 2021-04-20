# AI-TSP
AI: TSP

I\'ve created a basic class for the graph data structure. Its based on a python 
'dictionary' that uses the dictionays keys as nodes, and the values to store 
edges and weights (as 'tuples'). We have a couple methods, specifically edges and 
verticies, which each output a 'list'. 

I added a random graph generator to the initilization method. So now you can start playing with pathing 
as soon as you create the object. 

I\'m not sure how you want to work out the pathing. 

Per wikipedia, 

"A greedy strategy for the travelling salesman problem (which is of a 
high computational complexity) is the following heuristic: "At each step of 
the journey, visit the nearest unvisited city." This heuristic does not 
intend to find a best solution, but it terminates in a reasonable number of 
steps; finding an optimal solution to such a complex problem typically 
requires unreasonably many steps." 

So the pathing algorithim will need to keep a record of the cities its visited
along the way g(x). You have a path forward method in the class which you can 
use to generate the edges and distances of each step, until the class reaches
its origin. I\'ll give Graph_Class the ability to track and visualize your path
as you go and set the Print method to produce that output that path.
The greedy algo can call Print once it\'s done. 

Sample Implementation: Pathing by moving to the first never visited node.

```
def greedy(visited, options, start):
    if not visited:
        visited.append(start)
        print("Start: %s" % visited)
    while len(visited) != len(known_nodes):
        for iteration, option in enumerate(options):
            if option[0] not in known_nodes:
                known_nodes.append(option[0])
            if option[0] not in visited:
                visited.append(option[0])
                greedy(visited, graph.path_forward(iteration), start)

    print("Done!")
    return visited_nodes

from Graph_Class import Graph
num = 7
visited_nodes = []
known_nodes = []   
graph = Graph(nodes = num)
path = greedy(visited_nodes,graph.options, graph.location)                
``` 

I'm still going to cleanup the visualization a bit so it renders in a single
output. 

AJ Task List:
- [x] Graph Class
- [x] Random Graph Generator
- [x] Graph Visualizer
 
 KG Task List
 - [] Greedy Algorithim 




