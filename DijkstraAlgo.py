def getLeastCostNode(leastCosts, explored):
    nodesToSearch = [x for x in leastCosts.keys() if x not in explored]
    if nodesToSearch == []:
        return None
    min = leastCosts[nodesToSearch[0]]
    minNode = nodesToSearch[0]
    for node in nodesToSearch:
        if leastCosts[node]<min:
            min = leastCosts[node]
            minNode = node
    return minNode


graph = {
    "start": {"a": 5, "b": 1, "c": 10},
    "a": {"d": 2},
    "b": {"a": 1, "d": 7},
    "c": {"d": 1},
    "d": {"e": 3},
    "e": {"finish": 2},
    "finish": {}
}

leastCosts = {}
parents = {}
explored = []
currentNode = ""

if not(explored):
    leastCosts.update(graph["start"])
    for node in leastCosts.keys():
        parents[node] = "start"

while True:
    currentNode = getLeastCostNode(leastCosts, explored)
    if not(currentNode):
        break
    explored.append(currentNode)
    for neighbour in graph[currentNode].keys():
        costCurrentToNeighbour = graph[currentNode][neighbour]
        costStartToNeighbour = leastCosts[currentNode] + costCurrentToNeighbour
        if costStartToNeighbour < leastCosts.get(neighbour, float("inf")):
            leastCosts[neighbour] = costStartToNeighbour
            parents[neighbour] = currentNode

print("The least cost to the finish is:", leastCosts["finish"])
print("Follow this path -")
path = []
traceBack = "finish"
while traceBack != "start":
    traceBack = parents[traceBack]
    path.append(traceBack)
for i in path[::-1]:
    print(i, "->", end = " ")
print("finish")