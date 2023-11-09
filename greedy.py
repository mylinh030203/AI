import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbors):
        self.graph[node] = neighbors

def greedy(graph_data, start, goal, h):
    visited = set()
    path = []
    costArr = []
    current_node = start

    while current_node != goal:
        visited.add(current_node)
        neighbors = graph_data[current_node]
        neighbors = sorted(neighbors, key=lambda x: h(x[0]))
        
        # để kiểm tra xem có tìm thấy một đỉnh kề chưa thăm hay không
        found = False
        
        for neighbor, cost in neighbors:
            if neighbor not in visited:
                path.append(current_node)  # Convert cost to integer
                costArr.append(int(cost))
                current_node = neighbor
                found = True
                break

#Điều kiện kiểm tra xem có đỉnh kề nào chưa được thăm (biến found là False) hay không. Nếu không có đỉnh kề nào chưa được thăm, nghĩa là đã duyệt qua tất cả các đỉnh kề của current_node mà không tìm thấy đỉnh nào có thể thăm tiếp theo.
        if not found:
            if path:
                # thực hiện backtracking, quay lại đỉnh trước đó
                #lấy và loại bỏ phần tử cuối cùng của danh sách path, và [0] lấy đỉnh từ cặp giá trị (node, cost). Đỉnh này được gán cho current_node.
                current_node = path.pop()[0]
            else:
                # không có đỉnh nào chưa thăm và cũng không có đỉnh trên đường đi để quay lại (nếu path rỗng), thì thoát khỏi vòng lặp while. Điều này có nghĩa là không có đường đi từ start đến goal trong đồ thị
                print("không có đường đi")
                break

    total_cost = sum(cost for cost in costArr)  # Sum the integer costs
    return path, total_cost




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

# Hàm đánh giá heuristic
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

# Tạo đối tượng đồ thị
my_graph = Graph()
for node, neighbors in graph_data.items():
    my_graph.add_edge(node, neighbors)

start_node = 'Arad'
goal_node = 'Bucharest'
result_path, result_cost = greedy(graph_data, start_node, goal_node, h)

print("Path:", result_path)
print("Total Cost:", result_cost)
