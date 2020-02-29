

def add_matrices(a, b):
    result = []
    # for row_i in range(len(a)):
    #     row = []
    #     for col_i in range(len(a[0])):
    #         row.append(a[row_i][col_i] + b[row_i][col_i])
    #     result.append(row)
    for row_a, row_b in zip(a, b):
        row = []
        for col_a, col_b in zip(row_a, row_b):
            row.append(col_a +col_b)
        result.append(row)
    return result

def sub_matrices(a, b):
    result = []
    for row_a, row_b in zip(a, b):
        row = []
        for col_a, col_b in zip(row_a, row_b):
            row.append(col_a - col_b)
        result.append(row)
    return result
