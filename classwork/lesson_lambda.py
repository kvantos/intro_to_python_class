from pprint import pprint

d = {"earth":["земля", 19999], "mars":["марс", 1999], "venus":{'distance': 199000}}
d = {"earth": "земля", "mars":"марс", "venus": "венера"}

print(d)
d['mecrury'] = "меркурий"
print(d)

if "earth" in d:
    print("Earth is found!")
    del d['earth']
else:
    print("Earth is missing!")

print(d)
if "earth" in d:
    print("Earth is found!")
    del d['earth']
else:
    print("Earth is missing!")
print(d)

if "земля" in d.values():
    print("Земля найдена!")
else:
    print("Земля не найдена!")


d['venus'] = "Венера"
print(d)

capitals = {"UA":"Kyiv"}

products = {'Apple' : ['iPod', 'iPad', 'iPhone', 'iBook']}
products['Apple'].append('iWatch')
print(products)

for key in d:
    print(key, '->', d[key])

for key in d.keys():
    print(key, '->', d[key])

for value in d.values():
    print(value)


student1 = {'name':"Alice", 'age':24, 'year':2, 'grant':1000}
student2 = {'name':"Bob", 'age':22, 'year':1}
student3 = {'name':"Bill", 'age':19, 'year':1}

group = [student1, student2, student3]

for student in group:
    student['year'] +=1

pprint(group)

for student in group:
    if 'grant' in student:
        student['grant'] += 500
    else:
        student['grant'] = 1000

#pprint.pprint(group)
#print(d)

print("-----------------")
# group.sort(key=lambda student: student['age'])
# pprint.pprint(group)
# ot bolshego k menshemu po grantu, potom po imeni
group.sort(key=lambda stud: (stud['grant'], stud['name']), reverse=True)
pprint(group)

