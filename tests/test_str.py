from pandas import DataFrame
from tests.helpers import ExprTestCase
from pylars.dsl import _


class TestStringExpr(ExprTestCase):

    def data(self):
        return DataFrame({
            "a": ["dog", "cat", "horse"],
            "b": ["banana", "orange", "apple"],
            "fold": ["yo", "YO", "Fluß"],
            "many": ["dog dog", "cat cat", "H H"]
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

    def test_capitalize(self):
        self.make_test_expr(_.a.capitalize(), [
            "Dog", "Cat", "Horse"
        ])

    def test_casefold(self):
        self.make_test_expr(_.fold.casefold(), [
            "yo", "yo", "fluss"
        ])

    def test_len(self):
        self.make_test_expr(_.a.len(), [
            3, 3, 5
        ])

    def test_upper(self):
        self.make_test_expr(_.a.upper(), [
            "DOG", "CAT", "HORSE"
        ])

    def test_lower(self):
        self.make_test_expr(_.a.upper().lower(), [
            "dog", "cat", "horse"
        ])

    def test_title(self):
        self.make_test_expr(_.many.title(), [
            "Dog Dog", "Cat Cat", "H H"
        ])
