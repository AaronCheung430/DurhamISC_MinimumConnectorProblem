# another file

print("I am prim")

import queue

def prim(graph):
    que = queue.PriorityQueue()
    mst = []
    visited = set()
    total_weight = 0

    # Generate edge information with tuple and push it to Priority Queue
    #for outer_key in graph.keys():
    #    for inner_key, inner_cost in graph[outer_key].items():
    #        que.put((inner_cost, outer_key, inner_key))

    starting_vertex = list(graph.keys())[0]

    for next_to, cost in graph[starting_vertex].items():
        if next_to not in visited:
            que.put((cost, starting_vertex, next_to))

    while not que.empty():
        edge = que.get()
        cost, frm, to = edge
        new_edge = (frm, to, cost)

        if to in visited:
            continue

        visited.add(frm)
        visited.add(to)
        mst.append(new_edge)
        total_weight += cost

        for next_to, cost in graph[to].items():
            if next_to not in visited:
                que.put((cost, to, next_to))

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


    mst_path, total_weight = prim(arg_graph)
    print(mst_path)
    print(total_weight)

    # pause the program to show graph
    input("enter to return to menu...")