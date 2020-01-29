from pandas import DataFrame
from tests.helpers import ExprTestCase
from pylars.exprdsl import *
from pylars.exprdsl import _


class TestConversionExpr(ExprTestCase):

    def data(self):
        return DataFrame({
            "str": ["1", "2", "3"],
            "int": [1, 2, 3],
            "flt": [1.0, 2.0, 3.0],
            "flt2": [1.1, 2.2, 3.3],
        })

    def test_str_to_int(self):
        self.make_test_expr(_.str.astype(int) == _.int,
                            [True, True, True])
        self.make_test_expr(_.str == _.int.astype(str),
                            [True, True, True])

    def test_str_to_flt(self):
        self.make_test_expr(_.str.astype(float) == _.flt,
                            [True, True, True])
        self.make_test_expr(_.str + ".0" == _.flt.astype(str),
                            [True, True, True])

    def test_int_to_flt(self):
        self.make_test_expr(_.int.astype(float) == _.flt,
                            [True, True, True])
        self.make_test_expr(_.int == _.flt.astype(int),
                            [True, True, True])

    def test_flt_round_int(self):
        self.make_test_expr(_.flt2.astype(int) == _.int,
                            [True, True, True])

    def test_concat_int_str(self):
        self.make_test_expr(_.int.astype(str) + "_" + _.str.astype(str),
                            ["1_1", "2_2", "3_3"])
