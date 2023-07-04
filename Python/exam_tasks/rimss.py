'''два файла in1 in2 с числами
неубывающая последовательность
отсортировать в файл out
без повторений
потом в out2 перевод с римскую сс'''
def checkio(data):
    ones = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
    tens = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
    hunds = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
    thous = ["","M","MM","MMM","MMMM"]

    t = thous[data // 1000]
    h = hunds[data // 100 % 10]
    te = tens[data // 10 % 10]
    o =  ones[data % 10]

    return t+h+te+o
f1=open('in1.txt')
f2=open('in2.txt')
f_out1=open('out11.txt','w+')
f_out2=open('out2.txt','w')
line1=f1.readline().rstrip()
line2=f2.readline().rstrip()
flag1=True
flag2=True
t=0
while flag1 and flag2:
    if line1=='':
        flag1=False
        break
    if line2=='':
        flag2=False
        break
    if int(line1)==int(t):
        line1=f1.readline().rstrip()
    elif int(line2) == int(t):
        line2 = f2.readline().rstrip()
    elif  int(line1)>int(line2) :
        f_out1.write(line2+'\n')
        t=line2
        line2=f2.readline().rstrip()
    elif int(line1)<int(line2):
        f_out1.write(line1+'\n')
        t=line1
        line1=f1.readline().rstrip()
    elif int(line1)==int(line2):
        f_out1.write(line1+'\n')
        t=line1
        line1=f1.readline().rstrip()
        line2=f2.readline().rstrip()

while flag1:
    if line1=='':
        flag1=False
        break
    if int(line1) != int(t):
        t=line1
        f_out1.write(line1+'\n')
    line1 = f1.readline().rstrip()
while flag2:
    if line2=='':
        flag2=False
        break
    if int(line2) != int(t):
        t=line2
        f_out1.write(line2+'\n')
    line2 = f2.readline().rstrip()
f1.close()
f2.close()
f_out1.close()
f_out1=open('out11.txt')
for line in f_out1:
    line=line.rstrip()
    f_out2.write(checkio(int(line))+'\n')



