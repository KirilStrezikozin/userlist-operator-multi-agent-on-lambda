import operator
from collections.abc import Callable
from functools import wraps
from typing import Any

from .exceptions import FilteringOperationNotSupportedException


def __filter_op_func(func: Callable[[Any, Any], Any]):
    @wraps(func)
    def inner(
        attr_name: str,
        attr_value: Any,
        op_name: str,
        filter_by: Any,
    ):
        try:
            return func(attr_value, filter_by)
        except TypeError:
            raise FilteringOperationNotSupportedException(attr_name, op_name, filter_by)

    return inner


FilterComparisonOp = {
    ">": __filter_op_func(operator.gt),
    "<": __filter_op_func(operator.lt),
    "=": __filter_op_func(operator.eq),
    "!=": __filter_op_func(operator.ne),
    ">=": __filter_op_func(operator.ge),
    "<=": __filter_op_func(operator.le),
}


FilterOp = {
    **FilterComparisonOp,
    "contains": __filter_op_func(operator.contains),
}
