from aws_lambda_powertools.utilities.typing import LambdaContext

from utils.logger import logger


@logger.inject_lambda_context
def lambda_handler(event: dict, context: LambdaContext) -> str:
    logger.info("Received request from user")
    logger.debug(event)
    return "hello world"
