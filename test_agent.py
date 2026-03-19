import asyncio
import sys
import os
from io import StringIO

# Load environment variables FIRST, before any boto3/bedrock imports
from dotenv import load_dotenv
load_dotenv()

from langchain_core.messages import HumanMessage
from graph.graph import graph

async def test_agent():
    """Test the agent with a sample query"""
    messages = []
    
    # Test query
    user_input = "Create a marketing strategy for a tech startup"
    print(f"Testing with input: {user_input}\n")
    
    messages.append(HumanMessage(content=user_input))
    try:
        result = await graph.ainvoke({"messages": messages})
        messages = result["messages"]
        print(f"Agent Response:\n{messages[-1].content}\n")
        return True
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = asyncio.run(test_agent())
    sys.exit(0 if success else 1)
