def checkio(data):

    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hunds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    thous = ["", "M", "MM", "MMM", "MMMM"]

    t = thous[data // 1000]
    h = hunds[data // 100 % 10]
    te = tens[data // 10 % 10]
    o = ones[data % 10]

    return t + h + te + o


with open("in1.txt") as in1, open("in2.txt") as in2, \
open("out.txt", "w") as out:

    num_1 = (in1.readline()).strip("\n")
    num_2 = (in2.readline()).strip("\n")

    while True:

        if num_1 and num_2 and int(num_1) == int(num_2):
            print(num_1, end="\n", file=out)
            print(num_1, end="\n", file=out)
            num_1 = (in1.readline()).strip("\n")
            num_2 = (in2.readline()).strip("\n")

        elif num_1 and num_2 and int(num_1) < int(num_2):
            print(num_1, end="\n", file=out)
            num_1 = (in1.readline()).strip("\n")

        elif num_1 and num_2 and int(num_1) > int(num_2):
            print(num_2, end="\n", file=out)
            num_2 = (in2.readline()).strip("\n")

        elif num_1:
            print(num_1, end="\n", file=out)
            num_1 = (in1.readline()).strip("\n")

        elif num_2:
            print(num_2, end="\n", file=out)
            num_2 = (in2.readline()).strip("\n")

        else:
            break


with open("out.txt") as file_in, open("out1.txt", "w") as file_out:

    for numb in file_in:
        print("{:^79}".format(checkio(int(numb))), end="\n", file=file_out)

