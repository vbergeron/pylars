from pandas import DataFrame
from tests.helpers import ExprTestCase
from pylars.exprdsl import *


class TestNumericExpr(ExprTestCase):

    def data(self):
        return DataFrame({
            "a": [1, 2, 3, 4],
            "b": [1, 2, 4, 8],
        })

    def test_add(self):
        self.make_test_expr(C("a") + C("b"),
                            [2, 4, 7, 12])

    def test_sub(self):
        self.make_test_expr(C("a") - C("b"),
                            [0, 0, -1, -4])

    def test_mul(self):
        self.make_test_expr(C("a") * C("b"),
                            [1, 4, 12, 32])

    def test_truediv(self):
        self.make_test_expr(C("a") / C("b"),
                            [1, 1, 0.75, 0.5])

    def test_floordiv(self):
        self.make_test_expr(C("a") // C("b"),
                            [1, 1, 0, 0])

    def test_modulo(self):
        self.make_test_expr(C("a") % C("b"),
                            [0, 0, 3, 4])

    def test_litteral(self):
        self.make_test_expr(C("a") % 2,
                            [1, 0, 1, 0])
        self.make_test_expr(C("a") % L(2),
                            [1, 0, 1, 0])
