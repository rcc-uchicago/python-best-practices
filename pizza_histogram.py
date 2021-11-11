import matplotlib.pyplot as plt

pizza_orders = [("pepperoni", 2), ("hawaiian", 7), ("pepperoni",8), ("cheese", 2), ("hawaiian", 20), ("sausage", 5), ("cheese", 10), ("bacon", 2)]


'''
'''
pizza_dict = {}
for order in pizza_orders:

    if order[0] in pizza_dict.keys():
        pizza_dict[order[0]] += order[1]
    else:
        pizza_dict[order[0]] = order[1]

for pizza_type, count in pizza_dict.items():
    print("{}: {}".format(pizza_type, count))


plt.bar(list(pizza_dict.keys()), pizza_dict.values())
plt.show()
