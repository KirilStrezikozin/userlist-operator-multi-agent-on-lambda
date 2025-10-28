import logging

from aws_lambda_powertools import Logger

logger = Logger()

# Configure the root strands logger
logging.getLogger("strands").setLevel(logging.INFO)
logging.basicConfig(
    format="%(levelname)s | %(name)s | %(message)s", handlers=[logging.StreamHandler()]
)
