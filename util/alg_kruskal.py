# alg_kruskal.py
# find MST using Kruskal's Algorithm

import time
import queue


graph = {
            "A": {"B": 7, "C": 9},
            "B": {"A": 7, "C": 6, "D": 19, "F": 14},
            "C": {"A": 9, "B": 6, "D": 11, "E": 14},
            "D": {"B": 19, "C": 11, "E": 10, "F": 13, "G": 27, "I": 23},
            "E": {"C": 14, "D": 10, "I": 15},
            "F": {"B": 14, "D": 13, "G": 25, "H": 16},
            "G": {"D": 27, "F": 25, "H": 20, "I": 28},
            "H": {"F": 16, "G": 20, "I": 17},
            "I": {"D": 23, "E": 15, "G": 28, "H": 17}
        }

# graph = {'A': {'B': '4', 'C': '4', 'D': '6', 'E': '6'}, 'B': {'A': '4', 'C': '2'}, 'C': {'B': '2', 'A': '4', 'D': '8'}, 'D': {'C': '8', 'A': '6', 'E': '9'}, 'E': {'A': '6', 'D': '9'}}

# initalise dict, put all nodes into dict
def init_nodes(graph):
    nodes_dic = dict()
    for i,j in zip(range(len(graph)),graph.keys()):
        nodes_dic[i] = {j}
    return nodes_dic

# store (start_node, end_node, weight) into tuple and all inside the list
def init_weight(graph):
    edge_list = []
    for i in graph.keys():
        for j in graph[i].keys():
            if i != j:
                edge_list.append((i,j,int(graph[i][j])))
    edge_list.sort(key = lambda x:x[-1],reverse = False)    # sort the list in ascending order
    return edge_list

def kruskal(graph):

    k_time = time.perf_counter()
    nodes = init_nodes(graph)
    edges = init_weight(graph)
    choice = []#以选取边的列表,choice:选择

    #判断边的首尾两顶点是否在同一个集合内，若不在，则构不成环，
    #将此边放入choice列表中
    for edge in edges:
        for i in nodes.keys():
            if edge[0] in nodes[i]:
                start_node = i
            if edge[1] in nodes[i]:
                end_node = i

        if start_node != end_node:
            nodes[start_node] = nodes[start_node] | nodes[end_node]
            del nodes[end_node]
            choice.append(edge)

    total_weight = sum([x[-1] for x in choice])

    num = time.perf_counter() - k_time
    output = f"{num:.15f}"

    return choice, total_weight, output


# second way of doing it, by using queue
def kruskal_queue():

    k_queue_time = time.time()
    que = queue.PriorityQueue()
    nodes = init_set(graph)
    choice = []

    #
    for i in list(graph.keys()):
        for next_to, cost in graph[i].items():
            que.put((int(cost), i, next_to))

    #
    while not que.empty():
        edge = que.get()
        cost, frm, to = edge

        #
        for i in nodes.keys():
            if edge[1] in nodes[i]:
                start_node = i
            if edge[2] in nodes[i]:
                end_node = i

        #
        if start_node != end_node:
            nodes[start_node] = nodes[start_node] | nodes[end_node]
            del nodes[end_node]
            new_edge = (frm, to, cost)
            choice.append(new_edge)

    print(choice)

    print(sum([x[-1] for x in choice]))

    print("Queue time:",time.time() - k_queue_time)

kruskal(graph)