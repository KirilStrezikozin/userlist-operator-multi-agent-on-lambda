from http import HTTPStatus
from typing import Any

from aws_lambda_powertools.event_handler.exceptions import ServiceError


class InvalidFilteringCriteriaException(ServiceError):
    def __init__(self) -> None:
        super().__init__(HTTPStatus.BAD_REQUEST, "Filtering operation is not supported")


class FilteringOperationNotSupportedException(ServiceError):
    def __init__(
        self,
        attr: str,
        op_name: str,
        filter_by: Any,
    ) -> None:
        super().__init__(
            HTTPStatus.BAD_REQUEST,
            f"Filtering operation '{op_name}' by '{filter_by}' on field '{attr}' is not supported",
        )
