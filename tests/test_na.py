from pandas import DataFrame
from tests.helpers import ExprTestCase
from pylars.dsl import _
import numpy as np


class TestNaExpr(ExprTestCase):

    def data(self):
        return DataFrame({
            "a": [1, 2, np.NaN]
        })

    def test_isna(self):
        self.make_test_expr(_.a.isna(), [False, False, True])
