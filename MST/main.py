import time

# Decorator function to measure execution time
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} took {execution_time:.6f} seconds to execute")
        return result
    return wrapper

def read_graph_from_file(file_path):
    graph = {}
    
    with open(file_path, 'r') as file:
        data = file.read()
        data = data.replace("{{", "").replace("}}", "")
        edges = data.split("}, {")
        for edge in edges:
            v1, v2, weight = map(float, edge.strip('{}').split(','))
            if v1 in graph:
                graph[v1].append((v2, weight))
            else:
                graph[v1] = [(v2, weight)]
            if v2 in graph:
                graph[v2].append((v1, weight))
            else:
                graph[v2] = [(v1, weight)]
    
    return graph

@timing_decorator
def find_minimum_spanning_tree_weight(graph):
    visited = set()
    min_heap = [(0, 1)]  # (weight, vertex)
    total_weight = 0
    
    while min_heap:
        weight, node = min_heap.pop(0)
        if node not in visited:
            visited.add(node)
            total_weight += weight
            for neighbor, edge_weight in graph[node]:
                if neighbor not in visited:
                    min_heap.append((edge_weight, neighbor))
        min_heap.sort(key=lambda x: x[0])
    
    return total_weight

# file_paths = ["1.txt", "2.txt", "3.txt", "4.txt", "5.txt","6.txt", "7.txt", "8.txt", "9.txt", "10.txt"]


# for file_path in file_paths:
#     graph = read_graph_from_file(file_path)
#     mst_weight = find_minimum_spanning_tree_weight(graph)
#     print(f"The weight of the minimum spanning tree ({file_path}) is:", mst_weight)

file_path = "10.txt"
graph = read_graph_from_file(file_path)
mst_weight = find_minimum_spanning_tree_weight(graph)
print(f"The weight of the minimum spanning tree ({file_path}) is:", mst_weight)


