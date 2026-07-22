def get_employee(emp_id: str) -> dict:
    """Mock tool to fetch employee data."""
    return {
        "employee_id": emp_id,
        "name": "Alice Smith",
        "role": "Senior Data Engineer",
        "department": "Commercial Analytics"
    }

def get_product(product_name: str) -> dict:
    """Mock tool to fetch product details."""
    return {
        "product_name": product_name,
        "therapeutic_area": "Oncology",
        "status": "Active",
        "launch_year": 2019
    }

def get_campaign(campaign_name: str) -> dict:
    """Mock tool to fetch marketing campaign details."""
    return {
        "campaign_name": campaign_name,
        "channel": "Omnichannel Digital",
        "status": "Live",
        "region": "Europe"
    }

def get_sales(country: str) -> dict:
    """Mock tool to fetch regional sales data."""
    return {
        "country": country,
        "sales": 125000,
        "currency": "EUR",
        "quarter": "Q2"
    }