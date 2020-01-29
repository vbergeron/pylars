from pandas import DataFrame
from tests.helpers import ExprTestCase
from pylars.dsl import _


class TestStringExpr(ExprTestCase):

    def data(self):
        return DataFrame({
            "animal": ["dog", "cat", "horse"],
            "fruit": ["banana", "orange", "apple"],
            "fold": ["yo", "YO", "Fluß"],
            "many": ["dog dog", "cat cat", "H H"]
        })

    def test_concat(self):
        self.make_test_expr(_.animal + _.fruit, [
            "dogbanana",
            "catorange",
            "horseapple"
        ])

    def test_concat_ws(self):
        self.make_test_expr(_.animal + " - " + _.fruit, [
            "dog - banana",
            "cat - orange",
            "horse - apple"
        ])

    def test_capitalize(self):
        self.make_test_expr(_.animal.capitalize(), [
            "Dog", "Cat", "Horse"
        ])

    def test_casefold(self):
        self.make_test_expr(_.fold.casefold(), [
            "yo", "yo", "fluss"
        ])

    def test_contains(self):
        self.make_test_expr(_.fold.contains("y"), [
            True, False, False
        ])

    def test_contains_regex(self):
        self.make_test_expr(_.fold.contains("[yY]"), [
            True, True, False
        ])

    def test_match(self):
        self.make_test_expr(_.fruit.match(".+e$"), [
            False, True, True
        ])

    def test_len(self):
        self.make_test_expr(_.animal.len(), [
            3, 3, 5
        ])

    def test_upper(self):
        self.make_test_expr(_.animal.upper(), [
            "DOG", "CAT", "HORSE"
        ])

    def test_lower(self):
        self.make_test_expr(_.animal.upper().lower(), [
            "dog", "cat", "horse"
        ])

    def test_title(self):
        self.make_test_expr(_.many.title(), [
            "Dog Dog", "Cat Cat", "H H"
        ])

    def test_isupper(self):
        self.make_test_expr(_.animal.upper().isupper(), [
            True, True, True
        ])

    def test_islower(self):
        self.make_test_expr(_.animal.lower().islower(), [
            True, True, True
        ])
