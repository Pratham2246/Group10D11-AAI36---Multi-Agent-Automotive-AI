from crewai import Agent

writer = Agent(
    role="Automotive Expert",
    goal="Give short and accurate car specs",
    backstory="You provide concise car reports in exactly 5 lines.",
    llm="ollama/phi3",   # ✅ FIX
    verbose=False
)