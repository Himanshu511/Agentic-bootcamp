import re

def choose_tool_and_args(question: str) -> tuple[str | None, str | None]:
    clean_q = question.lower().strip()
    
    if "employee" in clean_q:
        # Extract the employee ID digits (e.g., "101" from "Get employee 101")
        match = re.search(r'\d+', clean_q)
        arg = match.group() if match else "101"
        return "employee", arg
        
    elif "product" in clean_q:
        # Extract product name or default to a sample match
        parts = clean_q.split("product")
        arg = parts[1].strip().title() if len(parts) > 1 else "Brukinsa"
        return "product", arg
        
    elif "campaign" in clean_q:
        parts = clean_q.split("campaign")
        arg = parts[1].strip() if len(parts) > 1 else "germany_digital"
        return "campaign", arg
        
    elif "sales" in clean_q:
        # Extract the country name following "for"
        if "for" in clean_q:
            parts = clean_q.split("for")
            arg = parts[1].strip().title()
        else:
            arg = "Germany"
        return "sales", arg
        
    return None, None