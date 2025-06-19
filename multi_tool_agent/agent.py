from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from multi_tool_agent.competitive_gent import competitive_analysis_agent
from multi_tool_agent.prd_agent import prd_agent
from multi_tool_agent.market_agent import market_analysis_agent


MODEL_OPENAI_O3_MINI = "o3-mini"

root_agent = LlmAgent(
    
    model=LiteLlm(model=MODEL_OPENAI_O3_MINI),
    name="manager",
    instruction=(
        "You are a strategic product launch coordinator. Your job is to take a product concept "
        "from the user—including its name, description, and optional features—and orchestrate a team of agents. "
        "Delegate tasks to the Market Research Agent, Competitive Analysis Agent, Feature Definition Agent, "
        "and Marketing Agent. Once all tasks are complete, synthesize the responses into a single product launch summary. "
        "Ensure all agents receive the right context and return a cohesive, useful output for the user."
    ),
    description="Main coordinator agent for orchestrating the product launch workflow. "
        "It receives the initial product idea and delegates tasks to sub-agents.",
    tools=[],
    sub_agents=[competitive_analysis_agent, prd_agent, market_analysis_agent],
)