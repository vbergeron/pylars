from typing import Set, List
from pylars.expr.result import Result


class Expr:

    def is_compatible(self, schema: Set[str]) -> Result:
        raise NotImplementedError

    def get_name(self) -> str:
        raise NotImplementedError

    def compile(self, scope) -> List[str]:
        raise NotImplementedError
