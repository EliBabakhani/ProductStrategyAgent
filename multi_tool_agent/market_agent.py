from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

MODEL_OPENAI_O3_MINI = "o3-mini"

market_analysis_agent = LlmAgent(
    model=LiteLlm(model=MODEL_OPENAI_O3_MINI),
    name="market_analysis_agent",
    instruction=(        "You are a market research agent tasked with analyzing trends, customer pain points, and demand signals relevant to a new product idea. "
        "Using the product description and target audience, synthesize insights from historical data and public knowledge. "
        "Identify emerging trends, customer needs, seasonal behavior, and underserved gaps in the market. "
        "Format your findings as a structured report that includes actionable insights to guide product strategy and positioning."
    

    ),
    description=        "Agent that performs market research and trend analysis. It identifies customer needs, market gaps, and emerging patterns based on "
        "the product idea and target audience to support early-stage product planning."
   ,
    tools=[]
)
