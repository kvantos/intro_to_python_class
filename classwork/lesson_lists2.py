import string
import random

zz = [x**2 for x in range(1,100) if x%2]

print(zz)

alpha = [ chr(c) for c in range(ord('a'), ord('z')+1)]

print(alpha)

ss = "muhahaha"
vowels = [c for c in ss if c in 'aoiue']

print(vowels)

ll = [d for d in range(10)]
print(ll)

ll2 = [i**2 for i in ll]
print(ll2)

ll3 = [j**2 for j in [d for d in range(10)]]
print(ll3)

tt1 = 'aa bb cc'
tt2 = 'bb cc dd'

for cc in tt1.split():
    if cc in tt2.split():
        print(cc)

ccc = [cc for cc in tt1.split() if cc in tt2.split()]
print(ccc)

# list functions
mua = [i for i in range(1,101)]
print(mua)
print(sum(mua))
print(min(mua))
print(max(mua))

print("--------")
print( max([ random.randrange(1000) for ch in range(100)]))

print(any(mua)) # at least one is true
print(all(mua)) #