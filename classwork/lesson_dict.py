from pprint import pprint as pp

dd = {"ho":2, "ha":3, "we":1}

print(dd)

dd['re'] = 34
print(dd)
del dd['ho']
print(dd)

countries = {"UK":"London", "Japan":"Tokio", "France":"Paris", "Italy":"Rome"}

print(countries)

products = {'Soda':['CocaCola', 'Sprite', 'Fanta', 'Pepsi']}

for x in dd:
    print(x, '->',dd[x])

for x in dd.keys():
    print(x, '->',dd[x])

for v in dd.values():
    print(v)

student1 = {'name':'Bob', 'age':22, 'year':1, 'grant':1000}
student2 = {'name':'Alice', 'age':23, 'year':2}
student3 = {'name':'John', 'age':21, 'year':3}

group = [student1, student2, student3]

pp(group)

for st in group:
    if 'grant' in st:
        st['grant'] += 500
    else:
        st['grant'] = 1000

pp(group)