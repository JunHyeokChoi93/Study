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
    unknown_lst = []
    for i in range(node-1):
        node1,node2,count = input().split()
        node1=int(node1);node2=int(node2);count=int(count)
        if node1 not in node_dict.keys():
            node_dict[node1] = [node2]
        else:
            node_dict[node1].append(node2)
        if node2 not in node_dict.keys():
            node_dict[node2] = [node1]
        else:
            node_dict[node2].append(node1)
        x=[node1,node2]
        x.sort()
        edge_dict[tuple(x)] = count
        if count == -1:
            unknown_lst.append(tuple(x))
    route_lst = []
    elf_memory_lst = []
    for i in range(elves):
        init_node,final_node,memory = input().split()
        memory = int(memory)
        route = find_route(init_node,final_node,node_dict,[])
        summation_dict = {'summation':0,'unknown':[],'memory':memory, 'route':route}
        for j in range(len(route)-1):
            key = tuple(sorted([route[j],route[j+1]]))
            if edge_dict[key] != -1:
                summation_dict['summation'] ^= edge_dict[key]
            else:
                summation_dict['unknown'].append(key)
        elf_memory_lst.append(summation_dict)

# 1 - change / 0 - remain



'''
6 5
1 2 -1
1 3 1
4 2 7
6 3 0
2 5 -1
2 3 1
2 5 0
5 6 1
6 1 1
4 5 1
'''
