import sys
from heapq import heapify,heappush,heappop
def dijsktra(graph,source,destination):
    inf=sys.maxsize
    node_data={"A":{"cost":inf, "pred":[]},
               "B":{"cost":inf, "pred":[]},
               "C":{"cost":inf, "pred":[]},
               "D":{"cost":inf, "pred":[]},
               "E":{"cost":inf, "pred":[]},
               "F":{"cost":inf, "pred":[]},
               }
    node_data[source]["cost"]=0
    visited=[]
    temp=source
    for i in range(5):
        if temp not in visited:
            visited.append(temp)
            min_heap=[]
            for j in graph[temp]:
                if j not in visited:
                    cost=node_data[temp]["cost"] +graph[temp][j]
                    if cost < node_data[j]["cost"]:
                        node_data[j]["cost"]=cost
                        node_data[j]["pred"]=node_data[temp]["pred"]+list(temp)
                    heappush(min_heap,(node_data[j]["cost"],j))
        heapify(min_heap)
        temp=min_heap[0][1]
    print("shortest distance:" +str(node_data[destination]["cost"])) 
    print("shortest path" +str(node_data[destination]["pred"] +list(destination)))             



if __name__=="__main__":
    graph={
        "A":{"B":2, "C":12},
        "B":{"A":2,"C":4, "D":8},
        "C":{"A":4,"B":3,"D":2, "E":5},
        "D":{"B":8,"C":2, "E":11, "F":22},
        "E":{"C":5,"D":8, "F":1},
        "F":{"D":22,"E":1}
    }
    source="A"
    destination="F"
    dijsktra(graph,source,destination)
