from dotenv import load_dotenv
load_dotenv()
from crewai import Task, Crew
from researcher import researcher
from writer import writer

car_name = input("Enter car name: ")

research_task = Task(
    description=f"Find specifications of {car_name} (price, top speed, range)",
    agent=researcher,
    expected_output="Car specifications including price, top speed, and range"
)

write_task = Task(
    description=f"Write a structured report on {car_name}",
    agent=writer,
    context=[research_task],
    expected_output="Well-formatted car report"
)

crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    verbose=True
)

result = crew.kickoff()

print("\nFINAL OUTPUT:\n")
print(result)