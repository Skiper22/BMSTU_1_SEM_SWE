'''Есть файл in.txt. В нем записаны строки разной длины. Переписать каждую строку в out.txt с изменениями:
1) Если среди символов есть знак '#', то удалить его.
2) Если в изменной строке есть слова-полиндромы, то записать в конце их количество
Весь файл в память читать нельзя '''
f1=open('in.txt')
f2=open('out.txt','w')
for line in f1:
    flag=False
    line1=line.split()
    for i in line1:
        for j in i:
            if j=='#':
                flag=True
                line=line.replace(j,'')
    if flag:
        flag2=False
        k=0
        line3=line.split()
        for i in line3:
            if i==i[::-1]:
                flag2=True
                k+=1
        if flag2:
            line=line.rstrip()+' '+str(k)
    f2.write(line.rstrip()+'\n')
f1.close()
f2.close()