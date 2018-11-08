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


def checkVaild(matrixNodeNum, startPoint, stopPoint):
    return (startPoint < matrixNodeNum and startPoint < matrixNodeNum)

def storePath(lastJumpNode,startPoint,stopPoint):
    pathList = []
    pathPoint = stopPoint
    pathList.append(pathPoint)
    while(pathPoint != startPoint):
        pathPoint = lastJumpNode[pathPoint]
        pathList.append(pathPoint)
    return pathList

def TranslateNodeName2NodePos(graph,startNodeName,stopNodeName):
    startPoint = graph.nodeNum 
    stopPoint = graph.nodeNum
    NodeNameNum = len(graph.nodeName)
    for i in range(NodeNameNum):
        if(startNodeName == graph.nodeName[i]):
            startPoint = i
        if(stopNodeName == graph.nodeName[i]):
            stopPoint = i
    return startPoint,stopPoint # If name is wrong, it will  return error start and stop points


def findShortestPath(graph, startNode, stopNode,isNodeName=False):

    if(isNodeName):
        startPoint,stopPoint = TranslateNodeName2NodePos(graph,startNode,stopNode)

    if(checkVaild(graph.nodeNum, startPoint, stopPoint) != True):
        return 0,[]

    graphMatrix = graph.matrix
    nodeNum = graph.nodeNum
    dis = graphMatrix[startPoint][:] # record the shorted path to startPoint
    visited = np.zeros(nodeNum, dtype=np.int)
    lastJumpNode = np.zeros(nodeNum, dtype=np.int)    # record the last jump for certain node
   
    for i in range(0, nodeNum):
        if(dis[i] != 0):
            lastJumpNode[i] = startPoint

    for i in range(0, nodeNum):
        min = 0
        for j in range(nodeNum):    # find shortest path to start node
            if(visited[j] != 1 and isSmaller(dis[j], min)):
                min = dis[j]
                minPoint = j

        visited[minPoint] = 1

        for j in range(nodeNum):  # update node distance
            if(
                isConnect(dis[minPoint])
                and isConnect(graphMatrix[minPoint][j])
                and isSmaller(graphMatrix[minPoint][j] + min, dis[j])
                ):
                dis[j] = graphMatrix[minPoint][j] + min
                lastJumpNode[j] = minPoint
    
    #store the path
    pathList = storePath(lastJumpNode,startPoint,stopPoint)

    return dis[stopPoint], pathList


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

    
