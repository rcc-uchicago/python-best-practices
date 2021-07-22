import matplotlib.pyplot as plt

pizza_orders = [("pepperoni", 2), ("hawaiian", 7), ("pepperoni",8), ("cheese", 2), ("hawaiian", 20), ("sausage", 5), ("cheese", 10), ("bacon", 2)]


'''

'''
hist = {}
for pizza_type, num_orders in pizza_orders:
    if pizza_type in hist.keys():
        hist[pizza_type] += num_orders
    else:
        hist[pizza_type] = num_orders

for pizza, num_order in hist.items():
    print("{}: {}".format(pizza, num_order))


plt.bar(list(hist.keys()), hist.values())
plt.show()