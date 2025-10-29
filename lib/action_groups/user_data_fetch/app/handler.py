from aws_lambda_powertools.utilities.typing import LambdaContext

from .app import app, logger, tracer
from .tools import *  # noqa: F403


@logger.inject_lambda_context
@tracer.capture_lambda_handler
def lambda_handler(event: dict, context: LambdaContext):
    return app.resolve(event, context)
