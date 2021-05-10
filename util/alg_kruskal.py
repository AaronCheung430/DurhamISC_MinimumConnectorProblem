# alg_kruskal.py
# find MST using Kruskal's Algorithm

import time
import queue

# initalise dict, put all nodes into dict
def init_nodes(graph):
    nodes_dic = dict()
    for i,j in zip(range(len(graph)),graph.keys()):
        nodes_dic[i] = {j}
    return nodes_dic

# store (start_node, end_node, weight) into tuple and all inside the list
def init_weight(graph):
    edge_list = []
    for start_node in graph.keys():
        for end_node in graph[start_node].keys():
            if start_node != end_node:
                edge_list.append((start_node, end_node, int(graph[start_node][end_node])))
    edge_list.sort(key = lambda x:x[-1], reverse = False)    # sort the list in ascending order
    return edge_list

# kruskal's algorithm to find mst
def kruskal(graph):

    k_s_time = time.perf_counter()  # set timer
    nodes = init_nodes(graph)   # find all nodes
    edges = init_weight(graph)  # find edge list
    no_nodes = len(nodes)   # find number of nodes in graph
    no_edges = int(len(edges)/2)    # find number of edges in graph
    mst = []    # set up mst as a empty list

    # determine whether the first and last nodes of the edge are in the same value of the key in dict
    for edge in edges:  # iterate through each elements in the list
        for i in nodes.keys():  # iterate through each key in the dict
            if edge[0] in nodes[i]: # check is that element in the value of corresponding key in dict
                start_node = i  # store i in variable
            if edge[1] in nodes[i]:
                end_node = i

        # if not, it won't form a cycle, so it can be added to mst
        if start_node != end_node:  # check is start_node the same with end_node for
            nodes[start_node] = nodes[start_node] | nodes[end_node] # merage both nodes to start_node
            del nodes[end_node] # delete corresponding key and value in dict
            mst.append(edge)    # append corresponding edge to list

    total_weight = sum([x[-1] for x in mst])    # find the sum of all weight in mst
    k_r_time = time.perf_counter() - k_s_time   # calculate the running time
    k_f_time = f"{k_r_time:.15f}"   # format the running time

    # return a dict with algorithm info
    return {"Algorithm": "Kruskal's Algorithm (without queue)", "Number of Nodes": no_nodes, "Number of Edges": no_edges, "Computation Time": k_f_time, "Path Found": mst, "Minimal Weight": total_weight}

# another kruskal's algorithm to find mst, by using queue
def kruskal_queue(graph):

    k_queue_s_time = time.perf_counter()    # set timer
    que = queue.PriorityQueue() # set up a priority queue
    nodes = init_nodes(graph)   # find all nodes
    mst = []    # set up mst as a empty list

    # put all edges into que
    for i in list(graph.keys()):
        for next_to, cost in graph[i].items():
            que.put((int(cost), i, next_to))

    no_nodes = len(nodes)   # find number of nodes in graph
    no_edges = int(que.qsize()/2)    # find number of edges in graph

    # when que is not empty, run the following code
    while not que.empty():
        edge = que.get()    # get the first element in que, and it will be removed by default
        cost, frm, to = edge    # unpack edge

        # iterate through each key in the dict
        for i in nodes.keys():
            if edge[1] in nodes[i]: # check is that element in the value of corresponding key in dict
                start_node = i  # store i in variable
            if edge[2] in nodes[i]:
                end_node = i

        # determine whether the first and last nodes of the edge are in the same value of the key in dict
        if start_node != end_node:
            nodes[start_node] = nodes[start_node] | nodes[end_node]
            del nodes[end_node]
            new_edge = (frm, to, cost)  # reformat the edge into correct order
            mst.append(new_edge)

    total_weight = sum([x[-1] for x in mst])
    k_queue_r_time = time.perf_counter() - k_queue_s_time
    k_queue_f_time = f"{k_queue_r_time:.15f}"

    # return a dict with algorithm info
    return {"Algorithm": "Kruskal's Algorithm (with queue)", "Number of Nodes": no_nodes, "Number of Edges": no_edges, "Computation Time": k_queue_f_time, "Path Found": mst, "Minimal Weight": total_weight}
