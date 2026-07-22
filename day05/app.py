import tools

print("=" * 60)
print("Enterprise Simulation Assistant — Local Dispatch Router")
print("Supported Prefixes: 'calc', 'temp', 'bmi', 'currency', 'campaign'")
print("Type 'exit' to quit")
print("=" * 60)

while True:
    user_input = input("\nYou: ").strip()

    if user_input.lower() == "exit":
        break

    try:
        # Split input into command syntax structure
        parts = user_input.split()
        if not parts:
            continue
            
        command = parts[0].lower()

        # Route 1: Basic Calculator -> e.g., calc 10 + 5
        if command == "calc":
            _, val1, op, val2 = parts
            result = tools.calculator(float(val1), float(val2), op)
            print("Assistant:", result)

        # Route 2: Temperature Converter -> e.g., temp 37 c_to_f
        elif command == "temp":
            _, value, direction = parts
            result = tools.convert_temperature(float(value), direction)
            print("Assistant:", result)

        # Route 3: BMI Calculator -> e.g., bmi 70 1.75
        elif command == "bmi":
            _, weight, height = parts
            result = tools.calculate_bmi(float(weight), float(height))
            print("Assistant:", result)

        # Route 4: Currency Converter -> e.g., currency 100 usd inr
        elif command == "currency":
            _, amount, from_curr, to_curr = parts
            result = tools.convert_currency(float(amount), from_curr, to_curr)
            print("Assistant:", result)

        # Route 5: Domain Workflow Lookup -> e.g., campaign germany brukinsa
        elif command == "campaign":
            _, country, product = parts
            result = tools.lookup_pharma_campaign(country, product)
            print("Assistant:", result)

        else:
            print("Assistant: Command string unrecognized. Please leverage a proper tool routing prefix.")

    except ValueError:
        print("Assistant: Parsing error. Ensure numerical inputs are correct for calculation tools.")
    except Exception as e:
        print(f"Assistant: Operational parsing logic encountered an issue: {e}")
        