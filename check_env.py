import os
from dotenv import load_dotenv

print("=== Checking Environment Variables ===")
print(f"Before load_dotenv():")
print(f"  AWS_ACCESS_KEY_ID: {os.getenv('AWS_ACCESS_KEY_ID', 'NOT SET')}")
print(f"  AWS_SECRET_ACCESS_KEY: {os.getenv('AWS_SECRET_ACCESS_KEY', 'NOT SET')}")
print(f"  AWS_DEFAULT_REGION: {os.getenv('AWS_DEFAULT_REGION', 'NOT SET')}")

# Load from .env
result = load_dotenv()
print(f"\nload_dotenv() returned: {result}")

print(f"\nAfter load_dotenv():")
print(f"  AWS_ACCESS_KEY_ID: {os.getenv('AWS_ACCESS_KEY_ID', 'NOT SET')}")
print(f"  AWS_SECRET_ACCESS_KEY: {os.getenv('AWS_SECRET_ACCESS_KEY', 'NOT SET')[:10]}...")
print(f"  AWS_DEFAULT_REGION: {os.getenv('AWS_DEFAULT_REGION', 'NOT SET')}")

# Check .env file exists
import os.path
print(f"\n.env file exists: {os.path.exists('.env')}")
print(f"Current working directory: {os.getcwd()}")
