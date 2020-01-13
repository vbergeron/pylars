from typing import Set, List
from pylars.expr import Expr
from pylars.expr.result import Result
import operator


class UnaryExpr(Expr):
    lhs: Expr
    rhs: Expr

    def __init__(self, parent: Expr, ops):
        self.parent = parent
        self.ops = ops

    def is_compatible(self, schema: Set[str]) -> Result:
        return self.parent.is_compatible(schema)

    def compile(self, scope) -> List[str]:
        parent_c = self.lhs.compile(scope)
        return parent_c + [
            f"{scope.varname}_{self.varname} = {self.ops}(",
            f"    {scope.varname}_{self.parent.varname}",
            ")"
        ]

    def get_name(self, scope):
        return self.rhs.compile(scope) + ["NYI"]


class Not(UnaryExpr):
    def __init__(self, parent: Expr):
        super().__init__(parent, "operator.__neg__")
