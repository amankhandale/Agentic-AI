# src/agents/weather_agent.py

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage
from langchain.tools import tool

import requests
from src.config import OPENWEATHER_API_KEY, OLLAMA_MODEL

# Define the tool directly here (or keep in tools/ and import)
@tool
def get_weather(city: str) -> str:
    """Get current weather for a city."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        city_name = data['name']
        return f"The weather in {city_name} is {weather} with a temperature of {temp}°C."
    else:
        return f"Could not fetch weather for {city}. Error: {response.status_code}"

# Set up the LLM with tool calling
llm = ChatOllama(model=OLLAMA_MODEL, temperature=0.3)

# Bind tools to the LLM
tools = [get_weather]
llm_with_tools = llm.bind_tools(tools)

# System prompt
system_prompt = """
You are a helpful weather assistant. 
Use the get_weather tool when the user asks about weather in a city.
Be concise and friendly.
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    MessagesPlaceholder(variable_name="messages"),
])

# Create the agent chain
agent_chain = prompt | llm_with_tools

def run_weather_agent(query: str):
    """Run the weather agent and return the final answer."""
    messages = [HumanMessage(content=query)]
    
    while True:
        response = agent_chain.invoke({"messages": messages})
        
        # If no tool call, return the response
        if not response.tool_calls:
            return response.content
        
        # Otherwise, execute tool calls
        for tool_call in response.tool_calls:
            if tool_call["name"] == "get_weather":
                tool_result = get_weather.invoke(tool_call["args"])
                messages.append(response)  # Add assistant message
                messages.append({
                    "role": "tool",
                    "name": "get_weather",
                    "content": tool_result,
                    "tool_call_id": tool_call["id"]
                })
            else:
                return "Sorry, I encountered an unknown tool."