# Текстовый файл (in.txt), n строк, в каждой строке n элементов разделенных пробелами
# Задача: повернуть чётные (начиная с нулевого) контуры на один элемент по часовой, нечётные -
# против часовой (пока не останется один элемент или не останется вовсе)
# Потом удалить из этой матрицы столбцы, которые содержат максимальный по значению элемент
# Записать перекрученную матрицу в файл, потом пустую строчку, потом матрицу с удаленными столбцами
# Выходной файл out.txt


def to_right(source, start, size):
    # Correction
    c_i, c_j = start

    temp = source[c_i][size - 1 + c_j]

    for i in range(size - 1, 0, -1):
        source[c_i][i + c_j] = source[c_i][i - 1 + c_j]

    temp1 = source[size - 1 + c_i][size - 1 + c_j]

    for i in range(size - 1, 0, -1):
        source[i + c_i][size - 1 + c_j] = source[i - 1 + c_i][size - 1 + c_j]

    source[1 + c_i][size - 1 + c_j] = temp

    temp2 = source[size - 1 + c_i][c_j]

    for i in range(size - 1):
        source[size - 1 + c_i][i + c_j] = source[size - 1 + c_i][i + 1 + c_j]

    source[size - 1 + c_i][size - 2 + c_j] = temp1

    for i in range(size - 1):
        source[i + c_i][c_j] = source[i + 1 + c_i][c_j]

    source[size - 2 + c_i][c_j] = temp2


def to_left(source, start, size):
    # Correction
    c_i, c_j = start

    temp = source[c_i][c_j]

    for i in range(size - 1):
        source[c_i][i + c_j] = source[c_i][i + 1 + c_j]

    for i in range(size - 1):
        source[i + c_i][size - 1 + c_j] = source[i + 1 + c_i][size - 1 + c_j]

    for i in range(size - 1, 0, -1):
        source[size - 1 + c_i][i + c_j] = source[size - 1 + c_i][i - 1 + c_j]

    for i in range(size - 1, 0, -1):
        source[i + c_i][c_j] = source[i - 1 + c_i][c_j]

    source[1 + c_i][c_j] = temp


f_in = open('in.txt')
matrix = []
for i in f_in.readlines():
    matrix.append(list(map(int, i.strip().split())))
f_in.close()

count = 0
operation = to_right
for i in range(len(matrix), 1, -2):
    operation(matrix, (count, count), i)
    if operation == to_right:
        operation = to_left
    else:
        operation = to_right
    count += 1

f_out = open('out.txt', 'w')
for i in matrix:
    for j in i:
        print(j, end=' ', file=f_out)
    print(file=f_out)

maximum = matrix[0][0]

for i in matrix:
    for j in i:
        if j > maximum:
            maximum = j

to_remove = set()

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] == maximum:
            to_remove.add(j)

for rem in to_remove:
    for i in matrix:
        del i[rem]

print(file=f_out)

for i in matrix:
    for j in i:
        print(j, end=' ', file=f_out)
    print(file=f_out)

f_out.close()
