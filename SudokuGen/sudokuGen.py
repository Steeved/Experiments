from random import randrange as rand


def check(matrix):
    for y in matrix:
        a = []
        for x in y:
            if x in a:
                if x != 0: return True
            a.append(x)
    for x in range(len(matrix)):
        a = []
        for y in matrix:
            if y[x] in a:
                if y[x] != 0:
                    return True
            a.append(y[x])
    return False


def copy(matrix):
    new_matrix = []
    for a in matrix: new_matrix.append(a)
    return new_matrix


def shuffle(array):
    a = []
    while len(array) > 0:
        b = rand(0, len(array))
        a.append(array[b])
        del array[b]
    return a


def place(matrix, x, y):
    nums = shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9])
    x1 = x * 3
    x2 = x * 3 + 1
    x3 = x * 3 + 2
    y1 = y * 3
    y2 = y * 3 + 1
    y3 = y * 3 + 2
    matrix[y1][x1] = nums[0]
    matrix[y1][x2] = nums[1]
    matrix[y1][x3] = nums[2]
    matrix[y2][x1] = nums[3]
    matrix[y2][x2] = nums[4]
    matrix[y2][x3] = nums[5]
    matrix[y3][x1] = nums[6]
    matrix[y3][x2] = nums[7]
    matrix[y3][x3] = nums[8]
    if check(matrix):
        while check(matrix):
            nums2 = shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9])
            matrix[y1][x1] = nums2[0]
            matrix[y1][x2] = nums2[1]
            matrix[y1][x3] = nums2[2]
            matrix[y2][x1] = nums2[3]
            matrix[y2][x2] = nums2[4]
            matrix[y2][x3] = nums2[5]
            matrix[y3][x1] = nums2[6]
            matrix[y3][x2] = nums2[7]
            matrix[y3][x3] = nums2[8]
    return matrix


def swap_row(matrix, y1, y2):
    cur_elem = matrix[y1]
    matrix[y1] = matrix[y2]
    matrix[y2] = cur_elem
    return matrix


def swap_column(matrix, x1, x2):
    for cur_row in range(len(matrix)):
        cur_elem = matrix[cur_row][x1]
        matrix[cur_row][x1] = matrix[cur_row][x2]
        matrix[cur_row][x2] = cur_elem
    return matrix


def hide_nums(matrix, diff):  # Hides random numbers in the sudoku
    for cur_row in range(len(matrix)):
        for cur_col in range(diff - rand(0, 3)):
            hidden_elem = rand(0, 9)
            matrix[cur_row][hidden_elem] = 0
    return matrix


def write_to_file(matrix, file_name="sudoku.txt"):
    file = open(file_name, "w")
    sudoku = ''
    for cur_row in matrix:
        cur_line = ''
        for cur_elem in cur_row:
            if cur_elem == 0:
                cur_line += '[ ]'
            else:
                cur_line += '[' + str(cur_elem) + ']'
        sudoku += cur_line + '\n'
    file.write(sudoku)
    file.close()


def shuffle_nums(matrix):  # Shuffle the numbers of the valid Sudoku given to make a different one
    for a in range(200):
        quadrant_x = rand(0, 3) * 3
        quadrant_y = rand(0, 3) * 3
        row1 = quadrant_x + rand(0, 3)
        row2 = quadrant_x + rand(0, 3)
        col1 = quadrant_y + rand(0, 3)
        col2 = quadrant_y + rand(0, 3)
        matrix = swap_row(matrix, row1, row2)
        matrix = swap_column(matrix, col1, col2)
    return matrix


difficulties = {
    "easy": 3,
    "normal": 5,
    "hard": 7
}

print("Sudoku generator.\nAvailable difficulties: Easy Medium Hard")
difficulty = input('Difficulty: ')

try:
    hidden = difficulties[str(difficulty)]
except KeyError:
    input("Invalid Difficulty Selected!")
    exit()

board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]]

for row in range(3):
    for column in range(3):
        board = place(board, row, column)

solution = copy(board)
write_to_file(solution, 'solution.txt')
s_full_hidden = hide_nums(board, difficulties[str(difficulty)])
write_to_file(s_full_hidden)

input("Successfully created a sudoku in 'sudoku.txt'. Solution saved as 'solution.txt'")
