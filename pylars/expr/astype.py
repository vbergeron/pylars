from typing import Set
from pylars.expr import Expr
from pylars.expr.result import Result


class AsType(Expr):
    parent: Expr

    def __init__(self, parent: Expr, selftype):
        self.parent = parent
        self.selftype = selftype
        self.varname = parent.varname

    def is_compatible(self, schema: Set[str]) -> Result:
        return self.parent.is_compatible(schema)

    def get_name(self) -> str:
        return self.parent.name

    def compile(self, scope):
        return self.parent.compile(scope) + [
            f"{scope.varname}_{self.varname} = {scope.varname}_{self.varname}.astype({self.selftype.__name__})"
        ]
