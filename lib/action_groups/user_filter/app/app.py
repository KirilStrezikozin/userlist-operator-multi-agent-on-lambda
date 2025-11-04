from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.event_handler import BedrockAgentResolver

tracer = Tracer()
logger = Logger()
app = BedrockAgentResolver()
