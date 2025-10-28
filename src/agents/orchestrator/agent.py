from strands import Agent

from agents.user_filter import user_filter
from agents.user_provider import user_data_fetch
from core.agent_model import get_model

from .config import system_prompt
from .tools import final_analytics

model = get_model()

orchestrator_agent = Agent(
    model=model,
    system_prompt=system_prompt,
    # callback_handler=None,
    tools=[user_data_fetch, user_filter, final_analytics],
)
