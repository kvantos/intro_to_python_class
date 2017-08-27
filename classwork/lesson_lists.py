ll = [7,6,5,4,3,2,1]
id(ll)

ll2 = [10, 20, 30, 40, 50, 60, 70]

for i in range(3):
    ll2[i] *= 2
    print(ll2[i])

print(ll2)

for i in range(len(ll2)):
    ll2[i] = ll2[i]**2

print(ll2)

ll3 = ll2.copy()

for i in range(len(ll2)-1,-1,-1):
    if not ll2[i] % 3:
        del ll2[i]

print(ll2)

def is_even(num):
    return num % 2 == 0

def del_elements_by_cond(ll, condition):
    for i in range(len(ll)-1,-1,-1):
        if condition(ll[i]):
            del ll[i]

print(ll3)
del_elements_by_cond(ll3, is_even)
print(ll3)
