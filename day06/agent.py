import tools
from planner import choose_tool_and_args

def run_agent(question: str) -> str:
    tool_name, argument = choose_tool_and_args(question)
    
    if not tool_name:
        return "Agent: I couldn't determine which tool to use for that query."
        
    # Execute the appropriate mock tool
    if tool_name == "employee":
        result = tools.get_employee(argument)
    elif tool_name == "product":
        result = tools.get_product(argument)
    elif tool_name == "campaign":
        result = tools.get_campaign(argument)
    elif tool_name == "sales":
        result = tools.get_sales(argument)
    else:
        result = "Error: Unknown tool."
        
    return f"[Tool Executed: get_{tool_name} | Argument: {argument}]\nResult: {result}"