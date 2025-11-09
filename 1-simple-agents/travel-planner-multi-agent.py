import argparse
from crewai import Agent, Task, Crew, Process

DEFAULT_CITY = "Isfahan"
DEFAULT_COUNT = 8


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser("Simple multi-agent travel planner")
    p.add_argument("-c", "--city", default=DEFAULT_CITY, help="City to suggest attractions for")
    p.add_argument("-n", "--count", type=int, default=DEFAULT_COUNT, help="Number of attractions")
    p.add_argument("-q", "--quiet", action="store_true", help="Disable verbose crew output")
    return p.parse_args()

def main() -> None:
    args = parse_args()

    # Travel agent: suggests attractions for a city
    researcher = Agent(
        role="Travel Researcher",
        goal="Find the best attractions and activities",
        backstory="You are an expert at researching destinations and finding hidden gems."
    )

    planner = Agent(
        role="Itinerary Planner",
        goal="Create efficient and enjoyable travel plans",
        backstory="You excel at organizing activities into logical, time-efficient itineraries."
    )

    research_task = Task(
        description="Research the top {total_attractions} attractions in {city} and provide brief descriptions.",
        expected_output="A list of {total_attractions} attractions in {city} with descriptions and why they're worth visiting.",
        agent=researcher
    )

    planning_task = Task(
        description="Create a {days}-day itinerary for {city} using only the researched attractions provided in the context.",
        expected_output="A detailed {days}-day schedule with exactly {attractions_per_day} attractions per day, including timing, transportation tips, and meal suggestions.",
        agent=planner,
        context=[research_task]
    )
    
    crew = Crew(
        agents=[researcher, planner],
        tasks=[research_task, planning_task],
        process=Process.sequential
    )

    days = 2
    attractions_per_day = 2
    total_attractions = days * attractions_per_day

    # Build the dictionary using the variables
    inputs = {
        "city": args.city,
        "days": days,
        "attractions_per_day": attractions_per_day,
        "total_attractions": total_attractions
    }
    try:
        result = crew.kickoff(inputs=inputs)
        print(result)
    except Exception as e:
        print("Error running crew:", e)

if __name__ == "__main__":
    main()