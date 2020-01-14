import unittest
from pylars import Pylar


class ExprTestCase(unittest.TestCase):

    def make_test_expr(self, expr, expected):
        compute = (Pylar("testinput", self.data().columns)
                   .select(expr.alias("result"))
                   .compile())

        result = compute(testinput=self.data())

        self.assertEqual(expected,
                         list(result.result))

    def data(self):
        raise NotImplementedError
