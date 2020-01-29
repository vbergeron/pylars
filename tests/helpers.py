import unittest
from pylars import Pylar
from pylars.dsl import *


class ExprTestCase(unittest.TestCase):

    def make_test_expr(self, expr, expected, debug=False):
        if debug:
            c_args = {"export_file": "debug.py"}
        else:
            c_args = {}

        compute = (Pylar("testinput", self.data().columns)
                   .select(expr.alias("result"))
                   .compile(**c_args))

        result = compute(testinput=self.data())

        self.assertEqual(expected,
                         list(result.result))

    def data(self):
        raise NotImplementedError


class AggTestCase(unittest.TestCase):

    def make_test_agg(self, by, expr, expected):

        expr_name = expr.get_name()

        compute = (Pylar("testinput", self.data().columns)
                   .groupby(by, expr)
                   .select(result=C(expr_name))
                   .compile())

        result = compute(testinput=self.data())

        self.assertEqual(expected,
                         list(result.result))

    def data(self):
        raise NotImplementedError
