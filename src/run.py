# run.py  (place this in the root: Agentic-AI/run.py)

from src.agents.weather_agent import run_weather_agent

if __name__ == "__main__":
    print("🌤️ Weather Agent Ready! (Type 'quit' to exit)\n")
    while True:
        query = input("Ask about the weather: ")
        if query.strip().lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break
        try:
            response = run_weather_agent(query)
            print(f"\n🤖: {response}\n")
        except Exception as e:
            print(f"Error: {e}\n")