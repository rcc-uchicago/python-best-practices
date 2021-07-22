import os
import sys

parent_dir = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0, os.path.abspath(parent_dir))

from pizza_histogram import aggregate_orders


class TestPizzaHistogram:
    
    
    def test_aggregate_orders(self):
        pizza_orders = [
            ("pepperoni", 2),
            ("hawaiian", 7),
            ("pepperoni",8),
            ("cheese", 2),
            ("hawaiian", 20),
            ("sausage", 5),
            ("cheese", 10),
            ("bacon", 2)]
        
        hist = aggregate_orders(pizza_orders)
        
