class Node:
    # hàm khởi tạo, cho biết được các thuộc tính của class
    def __init__(self, name):
        self.name = name
        self.g = 0
        self.h = 0
        self.f = 0
        self.parent = None

def a_star(graph, start, goal):
    open_set = [start]
    closed_set = []

    while open_set:
        #node là biến đại diện cho mỗi phần tử trong open_set. node.f là giá trị thuộc tính f của node
        # có thể dùng sắp xếp rồi lấy phần tử đầu tiên
        # open_set.sort(key=lambda node: node.f, reverse=True)
        # current_node = open_set.pop(0)

        current_node = min(open_set, key=lambda node: node.f)

        if current_node.name == goal.name:
            path = []
            total_cost = current_node.f
            #lặp đến khi current_node== none
            while current_node:
                #Thêm tên của current_node vào danh sách path
                path.append(current_node.name)
                #Di chuyển sang nút cha của current_node
                current_node = current_node.parent
                #đảo ngược danh sách và trả về đường đi từ nút bắt đầu đến nút đích path[::-1]
            return path[::-1], total_cost

        open_set.remove(current_node)
        closed_set.append(current_node)
    #duyệt qua danh sách các nút kề của current_node và chi phí tương ứng để di chuyển từ current_node đến các nút kề
    #graph[current_node.name]: các phần tử có chỉ số = tên của curent_node: vd 'Arad': [('Sibiu', 140), ('Zerind', 75), ('Timisoara', 118)],: arad giống như chỉ số của 1 list bth chỉ số
        for neighbor_name, cost in graph[current_node.name]:
            #tạo 1 nút neighbor
            neighbor = Node(neighbor_name)
            neighbor.g = current_node.g + cost
            neighbor.h = h(neighbor_name)
            neighbor.f = neighbor.g + neighbor.h
            neighbor.parent = current_node

            if neighbor in closed_set:
                continue
#Tìm kiếm nút có cùng tên với neighbor_name trong open_set. Nếu tìm thấy, ta gán đối tượng đó cho existing_node_with_same_name, nếu không tìm thấy thì existing_node_with_same_name sẽ là None.
            existing_node_with_same_name = next((node for node in open_set if node.name == neighbor_name), None)
            #có thể so sánh với f tuy nhiên h = nhau nên có thể so sánh g
            if existing_node_with_same_name and neighbor.g >= existing_node_with_same_name.g:
                continue
            if existing_node_with_same_name:
                if neighbor.g < existing_node_with_same_name.g:
                    existing_node_with_same_name.g = neighbor.g
                    existing_node_with_same_name.f = neighbor.f
                    existing_node_with_same_name.parent = neighbor.parent
            else:
                open_set.append(neighbor)


    
    return None, 0

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
    # một từ điển (dictionary hoặc map) trong Python, được biểu diễn bằng cặp khóa-giá trị
    # H = {
    #     'A': 14,
    #     'B': 0,
    #     'C': 15,
    #     'D': 6,
    #     'E': 8,
    #     'F': 7,
    #     'G': 12,
    #     'H': 10,
    #     'I': 4,
    #     'K': 2
    # }
    return H[node_name]

# Dữ liệu đồ thị
graph = {
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

# graph = {
#     'A': [('C', 9), ('D', 7), ('E', 13), ('F', 20)],
#     'B': [],
#     'C': [('H', 6)],
#     'D': [('H', 8), ('E', 4)],
#     'E': [('K', 4), ('I', 3)],
#     'F': [('I', 6), ('G', 4)],
#     'G': [],
#     'H': [('K', 5)],
#     'I': [('K', 9), ('B', 5)],
#     'K': [('B', 6)]
# }

start_node = Node('Arad')
goal_node = Node('Bucharest')
# start_node = Node('A')
# goal_node = Node('B')

path, total_cost = a_star(graph, start_node, goal_node)
if path:
    print("Đường đi ngắn nhất là:", path)
    print("Tổng giá trị của đường đi là:", total_cost)
else:
    print("Không tìm thấy đường đi.")
