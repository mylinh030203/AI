import heapq

class Graph:
    def __init__(self):
        self.graph = {}
    #thêm một đỉnh và các đỉnh kề của nó vào đồ thị
    def add_edge(self, node, neighbors):
        self.graph[node] = neighbors

def ucs(graph, start, goal):
    #frontier là một tập hợp chứa các nút đang được xem xét, mỗi phần tử có định dạng (cost, node, path).
    frontier = [(0, start, [])]  # (cost, node, path)
    #explored là tập hợp chứa các nút đã được kiểm tra.
    explored = set()

#while chạy cho đến khi frontier trống. Lấy phần tử có chi phí thấp nhất từ frontier
    while frontier:
        cost, current, path = heapq.heappop(frontier)
#Nếu nút hiện tại đã được kiểm tra, bỏ qua nó.
        if current in explored:
            continue
#Thêm nút hiện tại vào đường đi.
        path = path + [current]
#Nếu nút hiện tại là nút đích, trả về đường đi và chi phí.
        if current == goal:
            return path, cost
#Đánh dấu nút hiện tại là đã kiểm tra.
        explored.add(current)
#Thêm các nút kề của nút hiện tại vào frontier nếu chúng chưa được kiểm tra.
        for neighbor, neighbor_cost in graph.get(current, []):
            if neighbor not in explored:
                heapq.heappush(frontier, (cost + neighbor_cost, neighbor, path))

    return None, None  # No path found

# Dữ liệu đồ thị
graph_data = {
    'Arad': [('Sibiu', 140), ('Zerind', 75), ('Timisoara', 118)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu', 80)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Drobeta', 120), ('Rimnicu', 146), ('Pitesti', 138)],
    'Rimnicu': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Vaslui', 142), ('Hirsova', 98)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Iasi', 92), ('Urziceni', 142)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)]
}

# Tạo đối tượng đồ thị, thêm các đỉnh và cạnh từ graph_data vào đối tượng này.
my_graph = Graph()
for node, neighbors in graph_data.items():
    my_graph.add_edge(node, neighbors)

# Điểm xuất phát và điểm đến
start_node = 'Arad'
goal_node = 'Bucharest'

# Tìm đường đi và chi phí
path, cost = ucs(my_graph.graph, start_node, goal_node)

# In kết quả
if path:
    print(f"Shortest path from {start_node} to {goal_node}: {path}")
    print(f"Cost: {cost}")
else:
    print(f"No path found from {start_node} to {goal_node}")
