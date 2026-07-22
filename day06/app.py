from agent import run_agent

print("Enterprise Agent Simulator Initialized.")
print("Try asking: 'Show sales for Germany', 'Get employee 101', or 'Find product Brukinsa'\n")

while True:
    user_prompt = input("You: ")
    if user_prompt.lower() == "exit":
        break
    response = run_agent(user_prompt)
    print(f"Assistant:\n{response}\n" + "-"*40)