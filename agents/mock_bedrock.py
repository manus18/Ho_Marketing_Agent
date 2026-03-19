"""Mock LLM for development/testing without AWS credentials"""
from langchain_core.messages import AIMessage
from typing import Any


class MockChatBedrock:
    """Mock implementation of ChatBedrock for testing"""
    
    def __init__(self, model: str = "mock-model", region_name: str = "us-east-1", **kwargs):
        self.model = model
        self.region_name = region_name
    
    def invoke(self, messages: list, **kwargs: Any) -> AIMessage:
        """Invoke mock LLM with messages"""
        response_text = """
# Marketing Strategy for Your Business

## Target Audience Analysis
- Identify your primary and secondary customer segments
- Create detailed buyer personas
- Research customer pain points and needs

## Marketing Channels
- Digital Marketing (Social Media, Email, Content Marketing)
- Traditional Marketing (Print, Events, Partnerships)
- Direct Sales and Outreach
- SEO and Search Engine Marketing

## Key Messaging & Positioning
- Define your unique value proposition
- Create compelling brand messaging
- Differentiate from competitors
- Build emotional connections with your audience

## Campaign Ideas
1. Launch awareness campaign on social media
2. Create valuable content marketing strategy
3. Implement email marketing campaigns
4. Develop partnerships with complementary businesses
5. Run targeted ads to key demographics

## Success Metrics & KPIs
- Customer Acquisition Cost (CAC)
- Return on Investment (ROI)
- Conversion Rates
- Customer Lifetime Value
- Brand Awareness Metrics
- Engagement Rates

## Implementation Timeline
- Month 1-2: Strategy finalization and team alignment
- Month 3-4: Campaign launch and initial optimization
- Month 5-6: Scale successful channels and adjust underperforming ones
- Month 7-12: Monitor, optimize, and plan next year's strategy

This is a mock response for development purposes.
"""
        return AIMessage(content=response_text)
    
    async def ainvoke(self, messages: list, **kwargs: Any) -> AIMessage:
        """Async invoke mock LLM"""
        return self.invoke(messages, **kwargs)
    
    def bind_tools(self, tools: list):
        """Mock bind_tools - just returns self"""
        return self
