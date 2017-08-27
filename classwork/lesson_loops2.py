import random


def revers_str2method(input_string):
    lstr = list(input_string)
    lstr.reverse()
    return "".join(lstr)


def max_random_numbers(num_of_numbers, lower_bound=100, upper_bound=200):

    max_rnd = lower_bound
    for i in range(num_of_numbers):
        rnd = random.randint(lower_bound, upper_bound)
        if rnd > max_rnd:
            max_rnd = rnd

    return max_rnd


def min_random_numbers(num_of_numbers, lower_bound=100, upper_bound=200):

    min_rnd = upper_bound
    for i in range(num_of_numbers):
        rnd = random.randint(lower_bound, upper_bound)
        if rnd < min_rnd:
            min_rnd = rnd

    return min_rnd


n = 10

while n > 0:
    print("hello there")
    n -= 1

while n < 100:
    print("muhhaha")
    n += 20



def fill_truck(max_volume, mbox_vol, mabox_vol):
    total_volume = 0

    while total_volume < max_volume:
        free_space = max_volume - total_volume
        box = random.randint(mbox_vol, mabox_vol)
        if free_space >= box:
            total_volume += box


print("hello mate, there 4 doors you need to choose from:")
print("1 you will lost")
print("2 you will lost your horse")
print("3 you will die")
print("4 your mind will blow up")

ll = ["I dont understand", "where are you??\n", "where is your horse?\n", "crap\n", "dancing\n"]
while True:
    choose = int(input("enter room number you want to go: "))
    if choose == 0:
        print("Goodby my little fellow")
        break

    if 0 <= choose <= 4:
        print(ll[choose])
    else:
        print(ll[0])
