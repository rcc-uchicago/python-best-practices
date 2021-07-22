import os
import sys
import pytest

parent_dir = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0, os.path.abspath(parent_dir))

from pizza_histogram import aggregate_orders


class TestPizzaHistogram:

    def test_aggregate_orders(self):
        pizza_orders = [
            ("pepperoni", 2),
            ("hawaiian", 7),
            ("pepperoni", 8),
            ("cheese", 2),
            ("hawaiian", 20),
            ("sausage", 5),
            ("cheese", 10),
            ("bacon", 2)]

        hist = aggregate_orders(pizza_orders)

        expected = {
            "pepperoni": 10,
            "hawaiian": 27,
            "cheese": 12,
            "sausage": 5,
            "bacon": 2,
            }

        if(self.dicts_differ(hist, expected)):
            pytest.fail()

    def test_aggregate_orders_empty(self):
        pizza_orders = []

        hist = aggregate_orders(pizza_orders)

        expected = {}

        if(self.dicts_differ(hist, expected)):
            pytest.fail()

    def test_aggregate_orders_repeated(self):
        pizza_orders = [
            ("pepperoni", 2),
            ("pepperoni", 8),
            ("pepperoni", 7)]

        hist = aggregate_orders(pizza_orders)

        expected = {
            "pepperoni": 17,
            }

        if(self.dicts_differ(hist, expected)):
            pytest.fail()

    def test_aggregate_orders_disjoint(self):
        pizza_orders = [
            ("pepperoni", 2),
            ("pineapple", 8),
            ("anchovies", 7)]

        hist = aggregate_orders(pizza_orders)

        expected = {
            "pepperoni": 2,
            "pineapple": 8,
            "anchovies": 7,
            }

        if(self.dicts_differ(hist, expected)):
            pytest.fail()

    def dicts_differ(self, dict1, dict2):
        if len(dict1) != len(dict2):
            return True

        for key in dict1:
            if key not in dict2:
                return True
            elif dict1[key] != dict2[key]:
                return True

        return False
