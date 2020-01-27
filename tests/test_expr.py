from pandas import DataFrame
from pandas.testing import assert_frame_equal
from pylars.exprdsl import *
from pylars.pylar import Pylar
import unittest


class TestCommonExpr(unittest.TestCase):
    def test_binary_named(self):
        expr = C("a") + C("b")
        self.assertEqual(expr.get_name(), "Plus(a,b)")

    def test_astype(self):
        data = DataFrame({"a": [1, 2, 3]})
        pipe = (Pylar("src", data.columns)
                .select(b=C("a").astype(str))
                .compile(export_file="debug.py"))

        res = pipe(data)

        assert_frame_equal(res, DataFrame({
            "b": ["1", "2", "3"]
        }))

    def test_astype_named(self):
        expr = C("a").astype(str)
        self.assertEqual(expr.get_name(), "a")
