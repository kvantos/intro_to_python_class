def pp(x):
    print("=======[]=======")
    print(x)
    print("------------------")

def foo(a):
    return a+1

rr = list(map(foo, [1,2,3]))

pp(rr)

ll = []
for i in [1,2,3]:
    ll.append(foo(i))

pp(ll)

lst = list(map(lambda x: x**2, [1,2,3]))
pp(lst)

lst = list(filter(lambda x: not x%2, [1,2,3,4,5,6,7,8,9]))
pp(lst)

word = "Welcome2Hillel"
ww = list(filter(lambda x: x.isupper(), word))
mm = list(map(lambda x: ord(x), ww))

pp(ww)
pp(mm)

planetes = ['venus', 'jupiter', 'mars', 'saturn']

def get_length(x):
    return len(x)

pp(planetes)
planetes.sort(key=get_length)
pp(planetes)

planetes2 = ['mars', 'venus', 'jupiter', 'saturn']

planetes2.sort(key=lambda elem: len(elem))
pp(planetes2)

planetes3 = ['mars', 'venus', 'jupiter', 'saturn']

planetes3.sort(key=len)
pp(planetes3)

dd = [-1,4,3,-5,2,-6]
dd.sort(key=abs)
pp(dd)

planetes4 = [['mercury', 123], ['mars', 3450], ['earth', 1900], ['venus', 4500]]
planetes4.sort(key=lambda elem:elem[1])
pp(planetes4)

planetes5 = [['mercury', 123], ['mars', 3450], ['earth', 1900], ['venus', 4500], ['earth', 1910]]
planetes5.sort(key=lambda elem: (len(elem[0]), elem[1]))
pp(planetes5)