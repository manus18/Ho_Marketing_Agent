import asyncio
import os
from dotenv import load_dotenv

# Load environment variables FIRST
load_dotenv()

# Ensure AWS credentials are set
if not os.getenv('AWS_DEFAULT_REGION'):
    os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'

from langchain_core.messages import HumanMessage
from graph.graph import graph


async def main():
    messages = []
    print("Marketing Agent CLI (type 'quit' to exit)\n")

    while True:
        user_input = input("You: ").strip()
        if not user_input or user_input.lower() in ("quit", "exit"):
            break

        messages.append(HumanMessage(content=user_input))
        result = await graph.ainvoke({"messages": messages})
        messages = result["messages"]

        print(f"\nAgent: {messages[-1].content}\n")


if __name__ == "__main__":
    asyncio.run(main())
