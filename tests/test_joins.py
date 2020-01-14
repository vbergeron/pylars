
from pandas import DataFrame
from pandas.testing import assert_frame_equal
from pylars.exprdsl import *
from pylars import Pylar
import unittest
import numpy as np


class TestJoins(unittest.TestCase):

    def test_inner_join(self):
        data_left = DataFrame({
            "key": [1, 2, 3, 4],
            "val_left": ["l", "l", "l", "l"]
        })
        data_right = DataFrame({
            "key": [1, 2],
            "val_right": ["r", "r"]
        })

        join = (Pylar("l", data_left.columns)
                .inner_join(Pylar("r", data_right.columns), on=["key"]))

        res = join.compile()(l=data_left, r=data_right)

        assert_frame_equal(res, DataFrame({
            "key": [1, 2],
            "val_left": ["l", "l"],
            "val_right": ["r", "r"]
        }))

    def test_left_join(self):
        data_left = DataFrame({
            "key": [1, 2, 3, 4],
            "val_left": ["l", "l", "l", "l"]
        })
        data_right = DataFrame({
            "key": [1, 2],
            "val_right": ["r", "r"]
        })

        join = (Pylar("l", data_left.columns)
                .left_join(Pylar("r", data_right.columns), on=["key"]))

        res = join.compile()(l=data_left, r=data_right)

        assert_frame_equal(res, DataFrame({
            "key": [1, 2, 3, 4],
            "val_left": ["l", "l", "l", "l"],
            "val_right": ["r", "r", np.NaN, np.NaN]
        }))

    def test_right_join(self):
        data_left = DataFrame({
            "key": [1, 2],
            "val_left": ["l", "l"]
        })
        data_right = DataFrame({
            "key": [1, 2, 3, 4],
            "val_right": ["r", "r", "r", "r"]
        })

        join = (Pylar("l", data_left.columns)
                .right_join(Pylar("r", data_right.columns), on=["key"]))

        res = join.compile()(l=data_left, r=data_right)

        assert_frame_equal(res, DataFrame({
            "key": [1, 2, 3, 4],
            "val_left": ["l", "l", np.NaN, np.NaN],
            "val_right": ["r", "r", "r", "r"]
        }))

    def test_outer_join(self):
        data_left = DataFrame({
            "key": [1, 2],
            "val_left": ["l", "l"]
        })
        data_right = DataFrame({
            "key": [3, 4],
            "val_right": ["r", "r"]
        })

        join = (Pylar("l", data_left.columns)
                .outer_join(Pylar("r", data_right.columns), on=["key"]))

        res = join.compile()(l=data_left, r=data_right)

        assert_frame_equal(res, DataFrame({
            "key": [1, 2, 3, 4],
            "val_left": ["l", "l", np.NaN, np.NaN],
            "val_right": [np.NaN, np.NaN, "r", "r"]
        }))
