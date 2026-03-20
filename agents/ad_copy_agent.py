import os
from langchain_aws import ChatBedrock
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool

_llm = None

def get_llm():
    """Lazy load ChatBedrock with AWS credentials."""
    global _llm
    if _llm is None:
        _llm = ChatBedrock(
            model="global.anthropic.claude-haiku-4-5-20251001-v1:0",
            region_name=os.getenv("AWS_REGION", "us-east-1")
        )
    return _llm


@tool
def create_ad_copy(business_name: str) -> str:
    """Generate ad copy for Google Ads and social media ads.
    Use this tool when the user asks for ad copy, advertising text,
    Google Ads, Facebook Ads, paid advertising, or PPC campaigns."""
    llm = get_llm()
    response = llm.invoke([
        HumanMessage(content=(
            f"Create ad copy for the business below, covering multiple ad formats.\n\n"
            f"**Google Search Ads** (3 variations):\n"
            f"- Headline 1 (max 30 chars)\n"
            f"- Headline 2 (max 30 chars)\n"
            f"- Headline 3 (max 30 chars)\n"
            f"- Description 1 (max 90 chars)\n"
            f"- Description 2 (max 90 chars)\n\n"
            f"**Social Media Ads** (2 variations for Facebook/Instagram):\n"
            f"- Primary text (compelling hook + value proposition)\n"
            f"- Headline\n"
            f"- Description\n"
            f"- CTA button suggestion\n\n"
            f"**LinkedIn Sponsored Post** (1 variation):\n"
            f"- Post text (professional tone, under 150 words)\n"
            f"- CTA\n\n"
            f"Make all copy persuasive, benefit-focused, and action-oriented.\n\n"
            f"Business Name: {business_name}\n\n"
            f"Generate ad copy:"
        ))
    ])
    return response.content