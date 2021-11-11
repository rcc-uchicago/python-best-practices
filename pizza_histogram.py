import matplotlib.pyplot as plt

pizza order = [("pepperoni", 2), ("hawaiian", 7), ("pepperoni",8), ("cheese", 2), ("hawaiian", 20), ("sausage", 5), ("cheese", 10), ("bacon", 2)]
pizza type = i

'''
'''
hist = {}
for i in pizza order:
    if i[pizza order] in hist.keys():
        hist[i[pizza order]] += i[1]
    else:

        hist[i[pizza order]] = i[1]

for k, v in hist.items():
    print("{}: {}".format(k, v))


plt.bar(list(hist.keys()), hist.values())
plt.show()
