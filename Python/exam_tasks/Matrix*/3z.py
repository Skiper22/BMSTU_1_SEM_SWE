def writeMatrix(matrix):
    for row in matrix:
        for elem in row:
            outFile.write(elem + ' ')
        outFile.write('\n')
    outFile.write('\n')

with open('in.txt', 'r') as inFile, open('out.txt', 'w') as outFile:
    matrix = []
    for row in inFile:
        count = 0
        newRow = []
        for elem in row:
            if elem == '*':
                count += 1
            elif elem == ' ':
                newRow.append(str(count))
                count = 0
        newRow.append(str(count))
        matrix.append(newRow)

    maxRow = 0
    for row in matrix:
        lenRow = len(row)
        if maxRow < lenRow:
            maxRow = lenRow

    lenMatrix = len(matrix)
    for i in range(lenMatrix):
        while len(matrix[i]) != maxRow:
            matrix[i].append('0')
    writeMatrix(matrix)

    lenMatrixColumn = len(matrix[0])
    sumList = []
    for i in range(lenMatrixColumn):
        sumColumn = 0
        for j in range(lenMatrix):
            sumColumn += int(matrix[j][i])
        sumList.append(sumColumn)

    for i in range(lenMatrixColumn - 1):
        flag = False
        for j in range(lenMatrixColumn - i - 1):
            if sumList[j] > sumList[j + 1]:
                sumList[j], sumList[j + 1] = sumList[j + 1], sumList[j]
                count = 0
                while count != lenMatrix:
                    matrix[count][j], matrix[count][j + 1] = matrix[count][j + 1], matrix[count][j]
                    count += 1
                flag = True
        if not flag:
            break
    writeMatrix(matrix)