import numpy as np
import graph as gp

def runExample():
    graph =gp.Graph()
    graph.matrix =[
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,0,0,0,0,0,0,0,0,0,0,0,0],	
        [2,0,0,0,0,0,0,0,0,0,0,0,0],	
        [0,4,2,0,0,0,0,0,0,0,0,0,0],	
        [0,6,9,0,0,0,0,0,0,0,0,0,0],	
        [0,7,5,0,0,0,0,0,0,0,0,0,0],	
        [0,0,0,1,5,0,0,0,0,0,0,0,0],	
        [0,0,0,8,4,6,0,0,0,0,0,0,0],	
        [0,0,0,4,4,2,0,0,0,0,0,0,0],	
        [0,0,0,0,0,0,9,5,0,0,0,0,0],	
        [0,0,0,0,0,0,4,3,5,0,0,0,0],	
        [0,0,0,0,0,0,0,1,7,0,0,0,0],	
        [0,0,0,0,0,0,0,0,0,3,5,4,0]
        ]
    graph.matrix = np.transpose(graph.matrix)
    graph.nodeNum = len(graph.matrix[0])
    graph.nodeName = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O']
    dis,pathList = gp.findShortestPath(graph,'A','M',True)
    gp.printPathInfo(dis,pathList,graph)

if __name__ == '__main__':
    runExample()
