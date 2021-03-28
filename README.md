# AI-TSP
AI: TSP

I\'ve created a basic class for the graph data structure. Its based on a python 
'dictionary' that uses the dictionays keys as nodes, and the values to store 
edges and weights (as 'tuples'). We have a couple methods, specifically edges and 
verticies, which each output a 'list'. 

Probably before you get started, I need to create a random path generator 
which I will include in the next push. I will get this done ASAP so the algo has
something to work with. 

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

AJ Task List:
- [] Random Graph Generator
- [] Graph Visualizer
 
 KG Task List
 - [] Greedy Algorithim 




