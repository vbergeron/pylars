from pandas import DataFrame
from pandas.testing import assert_frame_equal
from pylars import Pylar
import unittest
import numpy as np


class TestDrop(unittest.TestCase):

    def test_drop(self):
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
