def matrix_chain_multiplication(dimensions):
    n = len(dimensions)
    m = [[0] * n for _ in range(n)]

    for chain_length in range(2, n):
        for i in range(1, n - chain_length + 1):
            j = i + chain_length - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + dimensions[i - 1] * dimensions[k] * dimensions[j]
                if cost < m[i][j]:
                    m[i][j] = cost

    return m[1][n - 1]

def parse_matrix_chain_dimensions(filename):
    with open(filename, 'r') as file:
        data = file.read().strip()
    dimensions = [tuple(map(int, pair.strip(' {}').split(','))) for pair in data.split('}, {')]
    return [d[0] for d in dimensions] + [dimensions[-1][1]]

if __name__ == '__main__':
    file_name = '10.txt'  # Replace with your file name
    dimensions = parse_matrix_chain_dimensions(file_name)
    result = matrix_chain_multiplication(dimensions)
    print(f"The minimum number of multiplications required is: {result}")
