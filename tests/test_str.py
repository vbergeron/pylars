from pandas import DataFrame
from tests.helpers import ExprTestCase
from pylars.exprdsl import *
from pylars.exprdsl import _


class TestStringExpr(ExprTestCase):

    def data(self):
        return DataFrame({
            "a": ["dog", "cat", "horse"],
            "b": ["banana", "orange", "apple"],
        })

    def test_concat(self):
        self.make_test_expr(_.a + _.b, [
            "dogbanana",
            "catorange",
            "horseapple"
        ])

    def test_concat_ws(self):
        self.make_test_expr(_.a + " - " + _.b, [
            "dog - banana",
            "cat - orange",
            "horse - apple"
        ])
