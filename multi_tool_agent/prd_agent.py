from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

MODEL_OPENAI_O3_MINI = "o3-mini"

prd_agent = LlmAgent(
    model=LiteLlm(model=MODEL_OPENAI_O3_MINI),
    name="prd_agent",
    instruction=(        "You are a Product Requirements Document (PRD) generation agent. Your task is to take the refined product concept, "
        "along with insights from market and competitive analysis, and translate them into a well-structured PRD. "
        "The PRD should include sections such as problem statement, goals, key features, user stories, success metrics, "
        "and potential technical considerations. Make the output readable and organized, suitable for use by design, engineering, and marketing teams."
    

    ),
    description=        "Agent that generates a complete Product Requirements Document (PRD) based on a product concept, market insights, "
        "and competitive context. The PRD includes core features, user stories, goals, and measurable outcomes."
    ,
    tools=[]
)
