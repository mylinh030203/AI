# //check rang buoc cac phan tu ke nhau
# assignment chứa các biến đã tô
def is_valid_assignment(assignment, constraints):
    # //lap list rang buoc
    for constraint in constraints:
    # //check # trong list rang buoc
        var1, var2 = constraint.split('#')
        if var1 in assignment and var2 in assignment:
            if assignment[var1] == assignment[var2]:
                return False
    return True
# //backtracking_search
def backtracking_search(variables, domains, constraints, assignment):
    # //check gan gia tri trong map
    if len(assignment) == len(variables):
        # //check rang buoc
        if is_valid_assignment(assignment, constraints):
            # Lưu trữ một bản sao của phân bố giá trị nguoc lai retur rong
            return [assignment.copy()]  
        else:
            return []
# //list bien chua gan gia tri
    unassigned_vars = [var for var in variables if var not in assignment]
    # //get bien firstvar
    first_unassigned_var = unassigned_vars[0]
# //list gia tri true
    solutions = []
    for value in domains:
        # // Gán giá trị từ tập miền cho biến chưa được gán.
        assignment[first_unassigned_var] = value

        result = backtracking_search(variables, domains, constraints, assignment)
        # extend list in goi de quy
        solutions.extend(result)
# //remove first var de gAN GIA TRI cho bien khac
        assignment.pop(first_unassigned_var, None)

    return solutions

variables = ['WA', 'NT', 'Q', 'NSW', 'V', 'SA', 'T']
domains = ['red', 'green', 'blue']
constraints = ['SA#WA', 'SA#NT', 'SA#Q', 'SA#NSW', 'SA#V', 'WA#NT', 'MT#Q', 'Q#NSW', 'NSW#V']

initial_assignment = {}

solutions = backtracking_search(variables, domains, constraints, initial_assignment)

if solutions:
    print(f"Tìm thấy {len(solutions)} phân bố giá trị thỏa mãn:")
    for idx, solution in enumerate(solutions):
        print(f"Phân bố giá trị {idx + 1}:")
        for var, value in solution.items():
            print(f"{var}: {value}")
else:
    print("Không tìm thấy phân bố giá trị thỏa mãn các ràng buộc.")
