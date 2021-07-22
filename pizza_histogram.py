import matplotlib.pyplot as plt

o = [("pepperoni", 2), ("hawaiian", 7), ("pepperoni",8), ("cheese", 2), ("hawaiian", 20), ("sausage", 5), ("cheese", 10), ("bacon", 2)]


'''

'''
d = {}
for i in o:
    if i[0] in d.keys():
        d[i[0]] += i[1]
    else:

        d[i[0]] = i[1]

for k, v in d.items():
    print("{}: {}".format(k, v))


plt.bar(list(d.keys()), d.values())
plt.show()