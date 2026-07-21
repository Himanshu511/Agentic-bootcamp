from ollama import chat

# =====================================================================
# TASK: Experiment with 3 different system prompts. 
# Uncomment the ONE you want to test below!
# =====================================================================

# SYSTEM_PROMPT = "You are a Senior Data Engineer. Keep answers short, technical, and use Spark/SQL analogies."
# SYSTEM_PROMPT = "You are an expert Travel Planner. Keep responses enthusiastic, structured, and bulleted."
SYSTEM_PROMPT = "You are a Pharma Analytics Expert. Frame concepts around healthcare data, compliance, and HCP metrics."

# Initialize conversation history with the chosen system prompt identity
messages = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]

print("=" * 50)
print(f"Local AI Chatbot Activated!")
print(f"Active Identity: {SYSTEM_PROMPT}")
print("Type 'exit' to quit")
print("=" * 50)

while True:
    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    # 1. Append the new user message to the historical log
    messages.append({
        "role": "user",
        "content": question
    })

    # 2. Send the entire conversation history log to the model
    response = chat(
        model="llama3.2",
        messages=messages
    )

    assistant_response = response["message"]["content"]

    print("\nAssistant:")
    print(assistant_response)

    # 3. Append the assistant's response to the historical log so it remembers it next turn
    messages.append({
        "role": "assistant",
        "content": assistant_response
    })