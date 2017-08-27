from pprint import pprint
from collections import OrderedDict as odict

d = {i:chr(i) for i in range(10000 + 1)}

# pprint(d)

student1 = {'name':"Alice", 'age':24, 'year':2, 'grant':1000, "bonus":1000}

d = odict()
d['sdf'] = 23
for kk in student1.keys():
    d[kk] = student1[kk]

pprint(d)

for k, v in student1.items():
    print(k)
    print(v)

en2es_dict = {'world': 'mundo', 'language': 'idioms', 'bye':'hasta la vista'}

es2en_dict = {v:k for k, v in en2es_dict.items()}
pprint(es2en_dict)