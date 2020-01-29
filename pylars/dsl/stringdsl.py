from pylars.dsl import ExprDSL
from pylars.expr.stringops import *


class StringDSL:
    def __init__(self, expr):  # pragma: no cover
        self.expr = expr

    def capitalize(self):
        return ExprDSL(Capitalize(self.expr))

    def casefold(self):
        return ExprDSL(Casefold(self.expr))

    def len(self):
        return ExprDSL(Len(self.expr))

    def lower(self):
        return ExprDSL(Lower(self.expr))

    def upper(self):
        return ExprDSL(Upper(self.expr))

    def title(self):
        return ExprDSL(Title(self.expr))
