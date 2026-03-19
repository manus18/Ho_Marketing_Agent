from langchain_aws import ChatBedrock
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool

def get_llm():
    """Lazy load the LLM to avoid initialization errors at import time"""
    return ChatBedrock(
        model="anthropic.claude-3-haiku-20240307-v1:0",
        region_name="us-east-1"
    )


@tool
def create_marketing_strategy(business_name: str) -> str:
    """Create a comprehensive marketing strategy for a given business. 
    Use this when user asks for a marketing strategy for their business. 
    It could be campaign ideas, target audience, channels to use or anything related to marketing strategy. 
    The response should be detailed and actionable."""
   
    llm = get_llm()
    response = llm.invoke([
        HumanMessage(content=(
            f"Create a comprehensive marketing strategy for the given business.\n\n"
            f"Include:\n"
            f"- Target audience analysis\n"
            f"- Marketing channels\n"
            f"- Key messaging and positioning\n"
            f"- Campaign ideas\n"
            f"- Success metrics and KPIs\n"
            f"- Implementation timeline\n\n"
            f"Business Name: {business_name}\n\n"
            f"Create a comprehensive marketing strategy:"
        ))
    ])
    return response.content
