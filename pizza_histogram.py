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

def print_dict(dict):
    for k, v in dict.items():
        print("{}: {}".format(k, v))

def visualize(dict):
    #visualize items in dictionary with barplot
    plt.bar(list(dict.keys()), dict.values())
    plt.show()

print_dict(hist)
visualize(hist)
