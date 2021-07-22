import matplotlib.pyplot as plt
import argparse
import csv

def load_data(input_data):
    pizza_orders = []
    with open(input_data, newline='') as input_csv:
        input_csv = csv.reader(input_csv, quoting=csv.QUOTE_NONNUMERIC)
        next(input_csv, None)
        for row in input_csv:
            pizza_orders.append(tuple(row))
    return pizza_orders

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
    return plt

def show_hist(plt):
    plt.show()
    return

def save_hist(plt, output_filename):
    plt.savefig(output_filename)
    return

def main(pizza_orders_csv, save_fig, show_plot, filename):
    pizza_orders = load_data(pizza_orders_csv)
    agg_orders = aggregate_orders(pizza_orders)
    print_orders(agg_orders)
    generate_visualization(agg_orders)
    if save_fig: save_hist(plt, filename)
    if show_plot: show_hist(plt)
    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Aggregate pizza orders')
    parser.add_argument('-i', '--input_data', help='Please enter a path to where the data is stored', required=True)
    parser.add_argument('-d', '--display', help='Display the output histogram? Type True or False', required=False, default=True)
    parser.add_argument('-s', '--save', help='Save the output histogram? Type True or False', required=False, default=True)
    parser.add_argument('-o', '--out_filename', help='Select a filename your output histogram will be saved as.', required=False, default="orders.png")

    args = parser.parse_args()
    display =  False if args.display == "False" else True
    save = False if args.save == "False" else True
    main(args.input_data, save, display, args.out_filename)