from pandas import DataFrame
from pylars.exprdsl import *
from pylars.exprdsl import _
from tests.helpers import ExprTestCase


class TestBooleanExpr(ExprTestCase):

    def data(self):
        return DataFrame({
            "a": [True, True, False, False],
            "b": [True, False, True, False],
        })

    def test_eq(self):
        self.make_test_expr(_.a == _.b, [True, False, False, True])

    def test_ne(self):
        self.make_test_expr(_.a != _.b, [False, True, True, False])

    def test_and(self):
        self.make_test_expr(_.a & _.b, [True, False, False, False])

    def test_or(self):
        self.make_test_expr(_.a | _.b, [True, True, True, False])

    def test_not(self):
        self.make_test_expr(~_.a, [False, False, True, True])

    def test_lit_bool(self):
        self.make_test_expr(_.a & False, [False, False, False, False])
        self.make_test_expr(_.a | True, [True, True, True, True])
