from pandas import DataFrame
from pandas.testing import assert_frame_equal
from pylars.exprdsl import *
from pylars.exprdsl import _
from pylars.pylar import Pylar
import unittest


class TestNamedExpr(unittest.TestCase):
    def test_binary_named(self):
        expr = C("a") + C("b")
        self.assertEqual(expr.get_name(), "Plus(a,b)")

    def test_astype_named(self):
        expr = _.a.astype(str)
        self.assertEqual(expr.get_name(), "a")
