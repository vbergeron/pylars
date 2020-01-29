from typing import Set
from pylars.expr.binary_expr import *
from pylars.expr.unary_expr import *
from pylars.expr import *
from pylars.expr.result import Result
from pylars.utils import varname
import pylars.expr.agg_expr as agg
from functools import wraps


def ValueLitterals(f):
    @wraps(f)
    def wrap(self, other):
        if issubclass(type(other), Expr):
            return f(self, other)
        else:
            return f(self, L(other))
    return wrap


class ExprDSL(Expr):

    def __init__(self, expr):
        self.expr = expr
        self.varname = varname("COL", expr)

    def is_compatible(self, schema: Set[str]) -> Result:
        return self.expr.is_compatible(schema)

    def get_name(self) -> str:
        return self.expr.get_name()

    def compile(self, scope):
        return self.expr.compile(scope)

    def alias(self, name: str):
        return ExprDSL(Alias(self.expr, name))

    def astype(self, selftype):
        return ExprDSL(AsType(self.expr, selftype))

    def isna(self):
        return ExprDSL(IsNa(self.expr))

    def desc(self):
        return ExprDSL(Desc(self.expr))

    def __invert__(self):
        return ExprDSL(Not(self.expr))

    @ValueLitterals
    def __eq__(self, other):
        return ExprDSL(Equals(self.expr, other))

    @ValueLitterals
    def __ne__(self, other):
        return ExprDSL(NotEquals(self.expr, other))

    @ValueLitterals
    def __gt__(self, other):
        return ExprDSL(GreaterThan(self.expr, other))

    @ValueLitterals
    def __ge__(self, other):
        return ExprDSL(GreaterThanOrEquals(self.expr, other))

    @ValueLitterals
    def __lt__(self, other):
        return ExprDSL(LesserThan(self.expr, other))

    @ValueLitterals
    def __le__(self, other):
        return ExprDSL(LesserThanOrEquals(self.expr, other))

    @ValueLitterals
    def __and__(self, other):
        return ExprDSL(And(self.expr, other))

    @ValueLitterals
    def __or__(self, other):
        return ExprDSL(Or(self.expr, other))

    @ValueLitterals
    def __add__(self, other):
        return ExprDSL(Plus(self.expr, other))

    @ValueLitterals
    def __sub__(self, other):
        return ExprDSL(Minus(self.expr, other))

    @ValueLitterals
    def __mul__(self, other):
        return ExprDSL(Multiply(self.expr, other))

    @ValueLitterals
    def __mod__(self, other):
        return ExprDSL(Modulo(self.expr, other))

    @ValueLitterals
    def __truediv__(self, other):
        return ExprDSL(TrueDiv(self.expr, other))

    @ValueLitterals
    def __floordiv__(self, other):
        return ExprDSL(FloorDiv(self.expr, other))


def C(name: str):
    return ExprDSL(Column(name))


def L(name: str):
    return ExprDSL(Litteral(name))


def Count():
    return ExprDSL(agg.Count())


def Sum(name):
    return ExprDSL(agg.Sum(name))


def Mean(name):
    return ExprDSL(agg.Mean(name))


class Catalog:
    def __getattribute__(self, attr):
        return C(attr)


_ = Catalog()
