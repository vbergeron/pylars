from pylars.dsl import _
import unittest


class TestNamedExpr(unittest.TestCase):
    def test_binary_named(self):
        expr = _.a + _.b
        self.assertEqual(expr.get_name(), "Plus(a,b)")

    def test_astype_named(self):
        expr = _.a.astype(str)
        self.assertEqual(expr.get_name(), "a")
