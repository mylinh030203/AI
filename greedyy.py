# Tạo một hàm greedy sử dụng đồ thị và hàm heuristic
def greedy_with_heuristic(graph, start, goal, h):
    visited = set()
    current_node = start
    path = [current_node]
    total_cost = 0

    while current_node != goal:
        # Lấy danh sách láng giềng trong đồ thị
        neighbors = graph.get(current_node, [])
        # Kiểm tra nếu không có láng giềng
        if not neighbors:
            return None, 0

        # Sử dụng hàm heuristic để tìm láng giềng có giá trị h(n) thấp nhất
        nearest_neighbor, neighbor_cost = min(neighbors, key=lambda x: h(x[0]))

        # Kiểm tra xem đã thăm láng giềng này chưa
        if nearest_neighbor in visited:
            return None, 0

        # Đánh dấu láng giềng hiện tại là đã thăm
        visited.add(current_node)
        current_node = nearest_neighbor
        # Cập nhật đường đi hiện tại và tổng chi phí
        path.append(current_node)
        total_cost += neighbor_cost

    return path, total_cost

# Đồ thị và hàm heuristic
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

def h(node_name):
    H = {
        'Arad': 366,
        'Zerind': 374,
        'Oradea': 380,
        'Sibiu': 253,
        'Timisoara': 329,
        'Lugoj': 244,
        'Mehadia': 241,
        'Drobeta': 242,
        'Craiova': 160,
        'Rimnicu': 193,
        'Fagaras': 176,
        'Pitesti': 100,
        'Bucharest': 0,
        'Giurgiu': 77,
        'Urziceni': 80,
        'Hirsova': 151,
        'Eforie': 161,
        'Vaslui': 199,
        'Iasi': 226,
        'Neamt': 234
    }
    return H[node_name]

start_node = 'Arad'
goal_node = 'Bucharest'

path, total_cost = greedy_with_heuristic(graph_data, start_node, goal_node, h)

if path:
    print("Đường đi tối ưu:", ' -> '.join(path))
    print("Tổng chi phí:", total_cost)
else:
    print("Không tìm thấy đường đi từ", start_node, "đến", goal_node)
