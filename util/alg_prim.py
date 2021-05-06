# algo_prim.py
# find MST using Prim's Algorithm

import time
import queue

# prim's algorithm to find mst
def prim(graph):

    p_s_time = time.perf_counter()  # set timer
    starting_vertex = list(graph.keys())[0] # set starting_vertex to the first node
    seen_egdes = set()  # set up seen_egdes as a empty set
    weight_list = []    # set up mst as a empty list
    mst = []    # set up mst as a empty list
    total_weight = 0    # set variable to 0

    # to store edges that connect with that vertex into list and sort it
    def prim_weight(vertex):
        for next_to, weight in graph[vertex].items():
            if next_to not in seen_egdes:
                weight_list.append((starting_vertex,next_to,int(weight)))
        weight_list.sort(key = lambda x:x[-1],reverse = False)

    prim_weight(starting_vertex)    # call function to only add edges that connected to this node

    while weight_list:  # weight_list is not empty
        edge = weight_list[0]   # store the first element from the list to variable
        weight_list.pop(0)  # remove the first element in list
        frm, to, weight = edge    # unpack edge

        if to in seen_egdes:    # check is to in seen_edges
            continue    # start the loop again directly

        seen_egdes.add(frm) # add node to set
        seen_egdes.add(to)  # add node to set
        mst.append(edge)    # append corresponding edge to list
        total_weight += weight    # add weight into total_weight

        prim_weight(to) # call function to only add edges that connected to this node

    p_r_time = time.perf_counter() - p_s_time   # calculate the running time
    p_f_time = f"{p_r_time:.15f}"   # format the running time

    return mst, total_weight, p_f_time  # return mst, total weight, and running time


# another prim's algorithm to find mst, by using queue
def prim_queue(graph):

    t1 = time.perf_counter()    # set timer

    que = queue.PriorityQueue()
    mst = []
    visited = set()
    total_weight = 0

    starting_vertex = list(graph.keys())[0]

    for next_to, weight in graph[starting_vertex].items():
        if next_to not in visited:
            que.put((int(weight), starting_vertex, next_to))

    while not que.empty():
        edge = que.get()
        weight, frm, to = edge
        new_edge = (frm, to, weight)

        if to in visited:
            continue

        visited.add(frm)
        visited.add(to)
        mst.append(new_edge)
        total_weight += weight

        for next_to, weight in graph[to].items():
            if next_to not in visited:
                que.put((int(weight), to, next_to))

    num = time.perf_counter() - t1
    output = f"{num:.15f}"
    print("Queue Time:",output)

    return mst, total_weight






if __name__ == '__main__':
    # Undirected weighted graph
    arg_graph = {
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
    # arg_graph = {'A': {'B': 4, 'C': 4, 'D': 6, 'E': 6}, 'B': {'A': 4, 'C': 2}, 'C': {'B': 2, 'A': 4, 'D': 8}, 'D': {'C': 8, 'A': 6, 'E': 9}, 'E': {'A': 6, 'D': 9}}
    # arg_graph = {'A': {'B': '4', 'C': '4', 'D': '6', 'E': '6'}, 'B': {'A': '4', 'C': '2'}, 'C': {'B': '2', 'A': '4', 'D': '8'}, 'D': {'C': '8', 'A': '6', 'E': '9'}, 'E': {'A': '6', 'D': '9'}}

    # mst_path, total_weight = prim_queue(arg_graph)
    # print(mst_path)
    # print(total_weight)

    mst_path, total_weight, p_time = prim(arg_graph)
    print(mst_path)
    print(total_weight)
    print("Computation time is", p_time)

    # mst_path, total_weight = prim_queue(arg_graph)
    # print(mst_path)
    # print(total_weight)

    # pause the program to show graph
    input("enter to return to menu...")