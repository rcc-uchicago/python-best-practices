import matplotlib.pyplot as plt

pizzas = [("pepperoni", 2), ("hawaiian", 7), ("pepperoni",8), ("cheese", 2), ("hawaiian", 20), ("sausage", 5), ("cheese", 10), ("bacon", 2)]


'''
'''
hist = {}
for pizza in pizzas:
    if pizza[0] in hist.keys():
        hist[pizza[0]] += pizza[1]
    else:

        hist[pizza[0]] = pizza[1]

for k, v in hist.items():
    print("{}: {}".format(k, v))


plt.bar(list(hist.keys()), hist.values())
plt.show()
