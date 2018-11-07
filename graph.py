import numpy as np

class Graph:
    def __init__(self):
        self.nodeNum = 0
        self.matrix = []
        self.nodeName = []

def isSmaller(firstNum, secondNum):
    if(secondNum == 0):  # zero stand for the max number
        return True
    if(firstNum == 0):
        return False
    return (firstNum < secondNum)


def isConnect(dis):
    return (dis != 0)


def checkVaild(matrixNodeNum, point1, point2):
    return (point1 < matrixNodeNum and point1 < matrixNodeNum)


def findShortestPath(graph, point1, point2):
    if(checkVaild(graph.nodeNum, point1, point2) != True):
        return []

    graphMatrix = graph.matrix
    nodeNum = graph.nodeNum
    dis = graphMatrix[point1]  # record the shorted path to point1
    visited = np.zeros(nodeNum, dtype=np.int)
    # record the last jump for certain node
    lastJumpNode = np.zeros(nodeNum, dtype=np.int)
    pathPoint = point2  # used for finding node in shortest path

    for i in range(0, nodeNum):
        if(dis[i] != 0):
            lastJumpNode[i] = point1

    for i in range(0, nodeNum):
        min = 0
        for j in range(nodeNum):    # find shortest path
            if(visited[j] != 1 and isSmaller(dis[j], min)):
                min = dis[j]
                minPoint = j
                visited[minPoint] = 1
        for j in range(nodeNum):  # update node distance
            if(isConnect(graphMatrix[minPoint][j])
               and isSmaller(graphMatrix[minPoint][j] + min, dis[j])):
                dis[j] = graphMatrix[minPoint][j] + min
                lastJumpNode[j] = minPoint

    pathList = []
    pathList.append(pathPoint)
    while(pathPoint != point1):
        pathPoint = lastJumpNode[pathPoint]
        pathList.append(pathPoint)
    return dis[point2], pathList


def printPathInfo(dis, pathList,graph):

    pathLen = len(pathList)

    if(graph.nodeNum <= len(graph.nodeName)):#print Node Name
        startNode = graph.nodeName[ pathList[pathLen-1] ]
        stopNode = graph.nodeName[ pathList[0] ]
        print("%s->%s distance:%d" %(startNode,stopNode,dis))
        for i in np.arange(pathLen-1, 0, -1):
            print("%s->" % graph.nodeName[ pathList[i] ], end="")
        print("%s" % graph.nodeName[ pathList[0] ])      
    else:
        startNode = pathList[pathLen-1]
        stopNode = pathList[0]
        print("%d->%d distance:%d" %(startNode,stopNode,dis))
        for i in np.arange(pathLen-1, 0, -1):
            print("%d->" % pathList[i], end="")
        print("%d" % pathList[0])

    
