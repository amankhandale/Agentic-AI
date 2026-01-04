# Agentic-AI [Development]
Status: ACTIVE_ITERATION

This is the Development Stage. Code here is experimental, bleeding-edge, and not yet verified for production.

# Branch Navigation
dev ← You are here (Feature builds)

test ➔ Performance Benchmarking

main ➔ Stable Releases

# What's New
Weather Agent that work on Local LLM  ( model: qwen2.5:7b )

Use this command in your terminal to run the Agent 
```
python -m src.run
```

# Note
Make sure you setup your .env file manually 

So paste in this in your .env file
```
OPENWEATHER_API_KEY=" USE YOUR API KEY "
OLLAMA_MODEL=qwen2.5:7b
```

# Project Structure
``` bash
Agentic-AI/
├── src/                    # All source code lives here
│   ├── agents/             # Agent logic & implementations
│   │   └── weather_agent.py
│   ├── tools/              # Reusable tools (API wrappers, functions, etc.)
│   │   └── tool.py         
│   ├── config.py           # Loads environment variables (.env)
│   └── main.py             # Alternative entry point
├── venv/                   # Virtual environment (gitignored)
├── .env                    # Your secrets: API keys, model name (never commit!)
├── .gitignore
├── requirements.txt        # Python dependencies (installation required for new users)
├── run.py                  # Main entry point → run with: python run.py
├── README.md               # You're reading it!
```
