from pandas import DataFrame
from tests.helpers import ExprTestCase
from pylars.dsl import _


class TestCompExpr(ExprTestCase):

    def data(self):
        return DataFrame({
            "a": [1, 2, 3, 4],
            "b": [1, 2, 4, 8],
        })

    def test_eq(self):
        self.make_test_expr(_.a == _.b,
                            [True, True, False, False])

    def test_ne(self):
        self.make_test_expr(_.a != _.b,
                            [False, False, True, True])

    def test_lt(self):
        self.make_test_expr(_.a < _.b,
                            [False, False, True, True])

    def test_le(self):
        self.make_test_expr(_.a <= _.b,
                            [True, True, True, True])

    def test_gt(self):
        self.make_test_expr(_.a > _.b,
                            [False, False, False, False])

    def test_ge(self):
        self.make_test_expr(_.a >= _.b,
                            [True, True, False, False])
