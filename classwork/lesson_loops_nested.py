for i in range(10):
    print("%i: " % i, end="")
    for j in range(10):
        print(j, end="")

    print("")

def pyphagore():
    for i in range(1, 10):
        for j in range(1, 10):
            print(i*j, end="\t")
        print("")


pyphagore()