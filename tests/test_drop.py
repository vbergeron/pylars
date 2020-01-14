from pandas import DataFrame
from pandas.testing import assert_frame_equal
from pylars.exprdsl import *
from pylars import Pylar
import unittest
import numpy as np


class TestOrderBy(unittest.TestCase):

    def test_orderby_simple(self):
        data = DataFrame({
            "val1": [2, 1, 4, 3],
            "val2": [1, 1, 2, 2]
        })

        test = (Pylar("test", data.columns)
                .drop("val1"))

        res = test.compile()(test=data)

        assert_frame_equal(res, DataFrame({
            "val2": [1, 1, 2, 2]
        }))
