import sys
import importlib.util

# First, try to import the module file directly
spec = importlib.util.spec_from_file_location("strategy_agent", r"C:\Users\manub\Downloads\MAS\agents\strategy_agent.py")
module = importlib.util.module_from_spec(spec)

try:
    spec.loader.exec_module(module)
    print("Module executed successfully")
    print("Module attributes:", [x for x in dir(module) if not x.startswith('_')])
    if hasattr(module, 'create_marketing_strategy'):
        print("create_marketing_strategy found:", module.create_marketing_strategy)
    else:
        print("create_marketing_strategy NOT found in module")
except Exception as e:
    import traceback
    print("Error executing module:")
    traceback.print_exc()
