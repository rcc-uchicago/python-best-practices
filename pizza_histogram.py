import matplotlib.pyplot as plt

pizza_orders = [("pepperoni", 2), ("hawaiian", 7), ("pepperoni",8), ("cheese", 2), ("hawaiian", 20), ("sausage", 5), ("cheese", 10), ("bacon", 2)]


def aggregate_orders(pizza_orders):
    hist = {}
    for pizza_type, num_orders in pizza_orders:
        if pizza_type in hist.keys():
            hist[pizza_type] += num_orders
        else:
            hist[pizza_type] = num_orders
    return hist

def print_orders(hist):
    print("Order Breakdown")
    print("---------------")
    for pizza, num_order in hist.items():
        print("{}: {}".format(pizza, int(num_order)))
    return

def generate_visualization(hist):
    plt.figure(figsize=(8, 6))
    plt.bar(list(hist.keys()), hist.values(), color='gold', hatch='O')
    plt.title("Daily Pizza Orders", fontsize=16)
    plt.xlabel("Pizza Type", fontsize=14); plt.ylabel("Total Orders", fontsize=14)
    plt.savefig("pizza_orders.png")
    plt.show()
    return

def main():
    agg_orders = aggregate_orders(pizza_orders)
    print_orders(agg_orders)
    generate_visualization(agg_orders)
    return


if __name__ == '__main__':
    main()