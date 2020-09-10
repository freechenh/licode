graph = dict()
graph["start"] = {}
graph["start"]['a'] = 6
graph["start"]['b'] = 2

graph['a'] = dict()
graph['a']["fin"] = 1

graph['b'] = dict()
graph['b']['a'] = 3
graph['b']['fin'] = 5

graph['fin'] = {}

infinity = float("inf")
costs = dict()
costs["a"] = 6
costs['b'] = 2
costs["fin"] = infinity

parents = dict()
parents['a'] = "start"
parents['b'] = "start"
parents['fin'] = None

processed = list()


def find_lowest_cost_node(costs):
    lower_cost = float("inf")
    lower_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lower_cost and node not in processed:
            lower_cost = cost
            lower_cost_node = node
    return lower_cost_node


node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
