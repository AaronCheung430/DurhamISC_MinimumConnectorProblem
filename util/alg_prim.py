# algo_prim.py
# find MST using Prim's Algorithm

import time
import queue

# prim's algorithm to find mst
def prim(graph):

    p_s_time = time.perf_counter()  # set timer
    starting_vertex = list(graph.keys())[0] # set starting_vertex to the first node
    seen_edges = set()  # set up seen_edges as a empty set
    weight_list = []    # set up mst as a empty list
    mst = []    # set up mst as a empty list
    total_weight = 0    # set variable to 0
    no_nodes = len(graph)   # find number of nodes in graph
    no_edges = 0   # set variable to 0

    # to store edges that connect with that vertex into list and sort it
    def prim_weight(vertex):
        for next_to, weight in graph[vertex].items():
            if next_to not in seen_edges:
                weight_list.append((vertex,next_to,int(weight)))
        weight_list.sort(key = lambda x:x[-1],reverse = False)

    prim_weight(starting_vertex)    # call function to only add edges that connected to this node

    while weight_list:  # weight_list is not empty
        no_edges += 1   # find the number of edges
        edge = weight_list[0]   # store the first element from the list to variable
        weight_list.pop(0)  # remove the first element in list
        frm, to, weight = edge    # unpack edge

        if to in seen_edges:    # check is to in seen_edges
            continue    # start the loop again directly

        seen_edges.add(frm) # add node to set
        seen_edges.add(to)  # add node to set
        mst.append(edge)    # append corresponding edge to list
        total_weight += weight    # add weight into total_weight

        prim_weight(to) # call function to only add edges that connected to this node

    p_r_time = time.perf_counter() - p_s_time   # calculate the running time
    p_f_time = f"{p_r_time:.15f}"   # format the running time

    # return a dict with algorithm info
    return {"Algorithm": "Prim's Algorithm (without queue)", "Number of Nodes": no_nodes, "Number of Edges": no_edges, "Computation Time": p_f_time, "Path Found": mst, "Minimal Weight": total_weight}

# another prim's algorithm to find mst, by using queue
def prim_queue(graph):

    p_queue_s_time = time.perf_counter()    # set timer
    que = queue.PriorityQueue() # set variable to priority queue
    starting_vertex = list(graph.keys())[0] # set starting_vertex to the first node
    mst = []    # set up mst as a empty list
    seen_edges = set() # set up seen_edges as a empty set
    total_weight = 0    # set variable to 0
    no_nodes = len(graph)   # # find number of nodes in graph
    no_edges = 0    # set variable to 0

    # to store edges that connect with the firat vertex into priority queue, and it will be sorted
    for next_to, weight in graph[starting_vertex].items():
        if next_to not in seen_edges:
            que.put((int(weight), starting_vertex, next_to))

    # loop when que is not empty
    while not que.empty():
        no_edges += 1   # find the number of edges
        edge = que.get()    # get the first element from que and store it to variable
        weight, frm, to = edge  # unpack edge
        new_edge = (frm, to, weight) # format new_edge

        if to in seen_edges:    # check is to in seen_edges
            continue    # start the loop again directly

        seen_edges.add(frm) # add node to set
        seen_edges.add(to)  # add node to set
        mst.append(new_edge)    # append corresponding edge to list
        total_weight += weight  # add weight into total_weight

        # to add edges that connect with the corresponding vertex into priority queue, and it will be sorted
        for next_to, weight in graph[to].items():
            if next_to not in seen_edges:
                que.put((int(weight), to, next_to))

    p_queue_r_time = time.perf_counter() - p_queue_s_time
    p_queue_f_time = f"{p_queue_r_time:.15f}"

    # return a dict with algorithm info
    return {"Algorithm": "Prim's Algorithm (with queue)", "Number of Nodes": no_nodes, "Number of Edges": no_edges, "Computation Time": p_queue_f_time, "Path Found": mst, "Minimal Weight": total_weight}
