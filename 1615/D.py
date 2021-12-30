import math
def find_route(init_node,final_node,node_dict,route_list = []):
    search_node = node_dict[init_node]
    search_node = [n for n in search_node if n not in route_list]
    route_list = route_list + [init_node]
    for node in search_node:
        if final_node == node:
            route_list = route_list + [node]
            break
        else:
            dum_list = find_route(node,final_node,node_dict,route_list)
        if final_node in dum_list:
            route_list = dum_list.copy()
            break
    return route_list

# edge_dict = {('1', '2'): -1,
#  ('2', '1'): -1,
#  ('1', '3'): 1,
#  ('3', '1'): 1,
#  ('4', '2'): 7,
#  ('2', '4'): 7,
#  ('6', '3'): 0,
#  ('3', '6'): 0,
#  ('2', '5'): -1,
#  ('5', '2'): -1}
# node_dict = {'1': ['2', '3'],
#  '2': ['1', '4', '5'],
#  '3': ['1', '6'],
#  '4': ['2'],
#  '6': ['3'],
#  '5': ['2']}
# x=find_route('2','3',node_dict,[])
problem_num = int(input())
for pro in range(problem_num):

    node,elves = map(int,input().split())
    node_dict = {}
    edge_dict = {}
    for i in range(node-1):
        node1,node2,count = input().split()
        count = int(count)
        if node1 not in node_dict.keys():
            node_dict[node1] = [node2]
        else:
            node_dict[node1].append(node2)
        if node2 not in node_dict.keys():
            node_dict[node2] = [node1]
        else:
            node_dict[node2].append(node1)
        edge_dict[node1, node2] = count
        edge_dict[node2, node1] = count
    elf_node_lst = []
    elf_edge_lst = []
    elf_memory_lst = []
    for i in range(elves):
        init_node,final_node,memory = input().split()
        memory = int(memory)
        route = find_route(init_node,final_node,node_dict,[])
        elf_node_lst.append(route)
        x=[]
        for j in range(len(route)-1):
            x.append(edge_dict[route[j],route[j+1]])
        elf_edge_lst.append(x)
        elf_memory_lst.append(memory)
    print(elf_node_lst)
    print(elf_edge_lst)
    print(elf_memory_lst)




