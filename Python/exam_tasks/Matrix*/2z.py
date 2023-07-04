#В файле записаны строки, состоящие из звёздочек и пробелов.
#Требуется сформировать числовую матрицу по следующему правилу: количество строк соответствует количеству строк в файле,
# а значения элементов показывают количество подряд идущих звёздочек в строке. В случае, если строки матрицы получаются
# разной длины, дополнить более короткие строки нулями до длины максимальной строки.
#Вывести в новый файл полученную матрицу.
#Затем отсортировать столбцы матрицы по возрастанию суммы их элементов и дописать изменённую матрицу в выходной файл
#после пустой строки.

with open('D:\прога\in.txt', 'r') as in_file:
    line = in_file.readline()
    max_count = 0
    while line:
        el = line.split()
        count = len(el)
        if max_count < count:
            max_count = count
        line = in_file.readline()

with open('D:\прога\in.txt', 'r') as in_file, open('D:\прога\out.txt', 'w') as out1_file:
    line = in_file.readline()
    while line:
        el = line.split()
        if max_count == len(el):
            for j in range(len(el)):
                print(len(el[j]),end=' ',file=out1_file)
            print('',file=out1_file)
        else:
            for j in range(len(el)):
                print(len(el[j]),end=' ',file=out1_file)
            print('0 '*(max_count-len(el)),end='',file=out1_file)
            print('',file=out1_file)
        line = in_file.readline()
    print('',file=out1_file)

with open('D:\прога\out.txt', 'r') as out2_file:
    line = out2_file.readline()
    columns = len(line.split())
    rows = 1
    while line:
        rows += 1
        line = out2_file.readline()

with open('D:\прога\out.txt', 'r+') as out2_file:
    matrix = []
    for column in out2_file:
        matrix.append(column.replace('\n', '').split())
    column_sum = [0]*columns
    for i in range(rows-3):
        for j in range(columns):
            column_sum[j] += int(matrix[i][j])
    sorted_matrix = []
    for row in matrix:
        pairs = [pair for pair in enumerate(row)]
        sorted_pairs = list(sorted(pairs,key=lambda p:column_sum[p[0]]))
        sorted_matrix.append([pair[1] for pair in sorted_pairs])

    for i in range (rows-2):
        for j in range(columns):
            print(sorted_matrix[i][j],end=' ',file=out2_file)
        print('',file=out2_file)