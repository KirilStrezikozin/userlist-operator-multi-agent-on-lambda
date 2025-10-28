from strands.models import BedrockModel

from core.config import config


def get_model() -> BedrockModel:
    return BedrockModel(
        region_name=config.AWS_REGION,
        model_id=config.AGENTS_MODEL_ID,
    )
