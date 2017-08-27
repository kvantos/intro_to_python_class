import random

ll = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]


def pm(maa):
    for i in range(len(maa)):
        for j in range(len(maa[i])):
            print(maa[i][j], end="\t")

        print("")


def mm(maa, num):
    for i in range(len(maa)):
        for j in range(len(maa[i])):
            maa[i][j] = maa[i][j]*num


print(id(ll))
pm(ll)
mm(ll, 10)
pm(ll)

print(id(ll))

n = 5
m = 5

strr = [0] * n
maa = []
for i in range(m):
    maa.append(strr.copy())

pm(maa)


def fill_maa(maa, from_n, to_n):

    for i in range(len(maa)):
        for j in range(len(maa[i])):
            rnd_n = random.randrange(from_n, to_n)
            maa[i][j] = rnd_n

fill_maa(maa, 10, 100)
pm(maa)


def print_chess_table():
    hh = "ABCDEFGH"
    dd = "12345678"

    for i in dd:
        for j in hh:
            print("%s%s" % (j, i), end="\t")

        print("")

print_chess_table()
