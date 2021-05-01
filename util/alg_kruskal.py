

# graph = {
#             "A": {"B": 7, "C": 9},
#             "B": {"A": 7, "C": 6, "D": 19, "F": 14},
#             "C": {"A": 9, "B": 6, "D": 11, "E": 14},
#             "D": {"B": 19, "C": 11, "E": 10, "F": 13, "G": 27, "I": 23},
#             "E": {"C": 14, "D": 10, "I": 15},
#             "F": {"B": 14, "D": 13, "G": 25, "H": 16},
#             "G": {"D": 27, "F": 25, "H": 20, "I": 28},
#             "H": {"F": 16, "G": 20, "I": 17},
#             "I": {"D": 23, "E": 15, "G": 28, "H": 17}
#         }



#初始化并查集，使每一个节点单独存在于一个集合中
def init_set(graph):
    set_dic = dict()
    for i,j in zip(range(len(graph)),graph.keys()):
        set_dic[i] = {j}

    return set_dic

#将边及权重以三元组 "（始点，终点，权重）"的形式存放在数列中，
#并按照权重大小进行由低到高排序
def init_distance(graph):
    distance_list = []
    for i in graph.keys():
        for j in graph[i].keys():
            if i != j:
                distance_list.append((i,j,graph[i][j]))
    distance_list.sort(key = lambda x:x[-1],reverse = False)
    return distance_list


nodes = init_set(graph)
edges = init_distance(graph)
choice = []#以选取边的列表,choice:选择

#判断边的首尾两顶点是否在同一个集合内，若不在，则构不成环，
#将此边放入choice列表中
for edge in edges:
    for i in nodes.keys():
        if edge[0] in nodes[i]:
            first = i
        if edge[1] in nodes[i]:
            second = i

    if first != second:
        nodes[first] = nodes[first] | nodes[second]
        del nodes[second]
        choice.append(edge)

print(choice)

print(sum([x[-1] for x in choice]))
