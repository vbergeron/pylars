from pandas import DataFrame
from tests.helpers import ExprTestCase
from pylars.exprdsl import *


class TestNumericExpr(ExprTestCase):

    def data(self):
        return DataFrame({
            "a": [1, 2, 3, 4],
            "b": [1, 2, 4, 8],
        })

    def test_eq(self):
        self.make_test_expr(C("a") == C("b"),
                            [True, True, False, False])

    def test_ne(self):
        self.make_test_expr(C("a") != C("b"),
                            [False, False, True, True])

    def test_add(self):
        self.make_test_expr(C("a") + C("b"),
                            [2, 4, 7, 12])

    def test_sub(self):
        self.make_test_expr(C("a") - C("b"),
                            [0, 0, -1, -4])

    def test_mul(self):
        self.make_test_expr(C("a") * C("b"),
                            [1, 4, 12, 32])
