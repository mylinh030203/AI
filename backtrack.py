#kiểm tra xem có thể tô màu một đỉnh cụ thể node bằng một màu cụ thể c hay không, dựa trên các đỉnh kề đã được tô màu trong color.
def can_color(graph, node, c, color):
    for neighbor in graph[node]:
        #Nếu tìm thấy một đỉnh kề đã được tô màu bằng màu c, trả về False nếu không thể tô màu node bằng màu c
        if color[neighbor] == c:
            return False
    return True

def color_map_util(graph, m, color, v, solutions):
    #Nếu v bằng len(graph), tức là tất cả các đỉnh đã được tô màu
    if v == len(graph):
        solutions.append(color.copy())
        return True

    node = list(graph.keys())[v]
    #lặp qua các màu khả dụng (từ 1 đến m+1) và thử tô màu cho đỉnh node hiện tạ
    for c in range(1, m+1):
       # Nếu có thể tô màu, hàm gọi đệ quy để tiếp tục với đỉnh tiếp theo. 
        if can_color(graph, node, c, color):
            color[node] = c
            color_map_util(graph, m, color, v+1, solutions)
            color[node] = 0

# khởi tạo một từ điển color với các giá trị màu ban đầu là 0.
def color_map(graph, m):
    n = len(graph)
    color = {node: 0 for node in graph}
#lời giải được lưu trữ trong danh sách solutions.
    solutions = []
#gọi hàm color_map_util để tìm tất cả các phân bố giá trị màu và lưu trữ chúng trong danh sách solutions.
    color_map_util(graph, m, color, 0, solutions)

    if not solutions:
        print("Không tìm thấy lời giải.")
        return None

    return solutions

# Ví dụ sử dụng
graph = {
    "WA": ["NT", "SA"],
    "NT": ["SA", "Q"],
    "SA": ["WA","NT","Q","NSW", "V"],
    "Q": ["NT", "SA", "NSW"],
    "NSW":["Q","SA","V"],
    "V":["SA","NSW"],
    "T":[]
}

num_colors = 3
results = color_map(graph, num_colors)

if results is not None:
    print(f"Tìm thấy {len(results)} phân bố giá trị thỏa mãn:")
    for idx, result in enumerate(results):
        print(f"Phân bố giá trị {idx + 1}:")
        for node, col in result.items():
            print(f"Đỉnh {node}: {col}")
        print()
else:
    print("Không tìm thấy phân bố giá trị thỏa mãn các ràng buộc.")

