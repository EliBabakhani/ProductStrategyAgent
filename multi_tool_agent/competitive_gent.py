from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

MODEL_OPENAI_O3_MINI = "o3-mini"

competitive_analysis_agent = LlmAgent(
    model=LiteLlm(model=MODEL_OPENAI_O3_MINI),
    name="competitive_analysis_agent",
    instruction=("You are an intelligent research agent specializing in competitive product analysis. "
        "Your task is to analyze and compare existing competitors relevant to a given product idea. "
        "You should identify competitors, extract key information such as feature sets, pricing strategies, strengths, weaknesses, and market positioning. "
        "Use publicly available knowledge to produce a clear, concise summary that highlights potential opportunities or differentiation strategies "
        "for the new product. Your response should be formatted and structured to support strategic decision-making."
    

    ),
    description="Agent that analyzes the competitive landscape for a given product or feature. "
        "It generates a comparative report based on existing competitors, including their strengths, weaknesses, and strategic position."
   ,
    tools=[]
)
