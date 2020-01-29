from helpers import AggTestCase
from pandas import DataFrame
from pylars.dsl import *
from pylars.dsl import _


class TestAgg(AggTestCase):
    def data(self):
        return DataFrame({
            "tag": ["a", "a", "b", "b"],
            "x": [1, 2, 3, 4]
        })

    def test_count(self):
        self.make_test_agg(["tag"], Count(), [2, 2])

    def test_sum(self):
        self.make_test_agg(["tag"], Sum("x"), [3, 7])

    def test_mean(self):
        self.make_test_agg(["tag"], Mean("x"), [1.5, 3.5])
