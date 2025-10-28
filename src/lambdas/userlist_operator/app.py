from aws_lambda_powertools.utilities.typing import LambdaContext

from agents.orchestrator import orchestrator_agent
from core.logger import logger


@logger.inject_lambda_context
def lambda_handler(event: dict, context: LambdaContext) -> str:
    logger.info("Received request from user")
    logger.debug(event)

    prompt = f"Filtering criteria:\n{event.get('prompt')}"
    response = orchestrator_agent(prompt)

    return str(response)
