def calculator(a: float, b: float, operation: str):
    if operation == "+": return a + b
    elif operation == "-": return a - b
    elif operation == "*": return a * b
    elif operation == "/":
        if b == 0: return "Error: Cannot divide by zero."
        return a / b
    return "Invalid basic calculator operation."

def convert_temperature(value: float, direction: str):
    """Direction should be 'c_to_f' or 'f_to_c'"""
    if direction.lower() == "c_to_f":
        return (value * 9/5) + 32
    elif direction.lower() == "f_to_c":
        return (value - 32) * 5/9
    return "Invalid direction. Use 'c_to_f' or 'f_to_c'."

def calculate_bmi(weight_kg: float, height_m: float):
    if height_m <= 0:
        return "Error: Height must be greater than zero."
    bmi = weight_kg / (height_m ** 2)
    
    # Determine classification bounds
    if bmi < 18.5: status = "Underweight"
    elif bmi < 25: status = "Normal weight"
    elif bmi < 30: status = "Overweight"
    else: status = "Obese"
    
    return f"BMI: {bmi:.2f} ({status})"

def convert_currency(amount: float, from_currency: str, to_currency: str):
    """Uses fixed simulation conversion rates for USD, EUR, INR"""
    # Base conversions scaled against 1 USD for demonstration
    rates = {
        "USD_TO_INR": 83.50,
        "INR_TO_USD": 0.012,
        "EUR_TO_INR": 90.20,
        "INR_TO_EUR": 0.011,
        "USD_TO_EUR": 0.92,
        "EUR_TO_USD": 1.09
    }
    pair = f"{from_currency.upper()}_TO_{to_currency.upper()}"
    if pair in rates:
        return f"{amount} {from_currency.upper()} = {amount * rates[pair]:.2f} {to_currency.upper()}"
    return f"Exchange pair {pair} not supported in fixed mock rules."

def lookup_pharma_campaign(country: str, product: str):
    """Mock domain tool matching your pharma analytics workflow"""
    mock_db = {
        ("germany", "brukinsa"): {"status": "Active", "channel": "Omnichannel (Email + Digital)", "target_hcps": 1250},
        ("germany", "drugx"): {"status": "Planning", "channel": "Webinars", "target_hcps": 450}
    }
    key = (country.lower(), product.lower())
    if key in mock_db:
        data = mock_db[key]
        return f"[Target System Data] Country: {country.upper()} | Product: {product.upper()} | Status: {data['status']} | Channel: {data['channel']} | Target HCPs: {data['target_hcps']}"
    return f"No active mock campaign configuration found for {product} in {country}."