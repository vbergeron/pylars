
from pandas import DataFrame
from pylars.exprdsl import *
from pylars.pandecl import Pandecl
import unittest


class TestNumericExpr(unittest.TestCase):

    def test_inner_join(self):
        data_left = DataFrame({
            "key": [1, 2, 3, 4],
            "val_left": ["l", "l", "l", "l"]
        })
        data_right = DataFrame({
            "key": [1, 2, 3, 4],
            "val_right": ["r", "r", "r", "r"]
        })

        join = (Pandecl(data_left.columns)
                .inner_join(Pandecl(data_right.columns), on=["key"]))

        print(join.compile())
