from pandas import DataFrame
from pandas.testing import assert_frame_equal
from pylars import Pylar
from pylars.dsl import _
import unittest
import numpy as np


class TestOrderBy(unittest.TestCase):

    def test_orderby_simple(self):
        data = DataFrame({
            "val1": [2, 1, 4, 3],
            "val2": [1, 1, 2, 2]
        })

        test = (Pylar("test", data.columns)
                .order_by(_.val1))

        res = test.compile()(test=data)

        assert_frame_equal(res, DataFrame({
            "val1": [1, 2, 3, 4],
            "val2": [1, 1, 2, 2]
        }))

    def test_orderby_many(self):
        data = DataFrame({
            "val1": [2, 1, 4, 3],
            "val2": [1, 1, 2, 2]
        })

        test = (Pylar("test", data.columns)
                .order_by(_.val2.desc(), _.val1))

        res = test.compile()(test=data)

        assert_frame_equal(res, DataFrame({
            "val1": [3, 4, 1, 2],
            "val2": [2, 2, 1, 1]
        }))
