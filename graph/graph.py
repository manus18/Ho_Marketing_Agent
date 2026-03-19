import os
from dotenv import load_dotenv

# Load environment variables FIRST, before any boto3/bedrock imports
load_dotenv()

from .state import AgentState
from .prompt import SYSTEM_PROMPT
from agents import tools as all_tools
from langchain_core.messages import SystemMessage
from langgraph.graph import StateGraph,START
from langgraph.prebuilt import ToolNode, tools_condition

# Use mock LLM if USE_MOCK_LLM environment variable is set
USE_MOCK = os.getenv('USE_MOCK_LLM', 'false').lower() == 'true'

if not USE_MOCK:
    try:
        from langchain_aws import ChatBedrock
    except ImportError:
        print("Warning: langchain_aws not available, using mock LLM")
        USE_MOCK = True

if USE_MOCK:
    from agents.mock_bedrock import MockChatBedrock

# Create LLM lazily to avoid initialization errors
_llm = None
_llm_with_tools = None

def get_llm():
    global _llm, _llm_with_tools
    if _llm is None:
        if USE_MOCK:
            print("Using MOCK LLM for development (set USE_MOCK_LLM=false for real Bedrock)")
            _llm = MockChatBedrock()
        else:
            from langchain_aws import ChatBedrock
            _llm = ChatBedrock(
                model="anthropic.claude-3-haiku-20240307-v1:0",
                region_name=os.getenv('AWS_DEFAULT_REGION', 'us-east-1')
            )
        _llm_with_tools = _llm.bind_tools(all_tools)
    return _llm_with_tools

async def agent_node(state:AgentState)->dict:
    """ Node function for the agent. It takes the conversation history and the other relevant information from the state and returns the next"""
    llm_with_tools = get_llm()
    messages = [SystemMessage(content=SYSTEM_PROMPT)] + state["messages"]
    response = await llm_with_tools.ainvoke(messages)
    return {"messages": [response]}

def build_graph()->StateGraph:
    builder = StateGraph(AgentState)

    builder.add_node("agent", agent_node)
    builder.add_node("tools", ToolNode(all_tools))
                     
    builder.add_edge(START, "agent")
    builder.add_conditional_edges("agent",tools_condition)
    builder.add_edge("tools", "agent")

    return builder.compile()

graph = build_graph()

