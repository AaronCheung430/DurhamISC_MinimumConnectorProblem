# compare.py
#

import numpy as np

def create_completed_dict(nodes):

    new_complete_graph = {}
    nodes_list = [node for node in range(nodes)]

    for starting_node in nodes_list:

        new_complete_graph[starting_node] = None


    print(new_complete_graph)
    # for nested dict
    print(nodes_list)
    weight = np.random.randint(1, 101)
    print(weight)
    # pass

create_completed_dict(5)

