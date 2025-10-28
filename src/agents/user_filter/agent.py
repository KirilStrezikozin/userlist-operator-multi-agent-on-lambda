from strands import Agent

from core.agent_model import get_model

from .config import system_prompt

model = get_model()

filter_agent = Agent(
    model=model,
    system_prompt=system_prompt,
    callback_handler=None,
)
