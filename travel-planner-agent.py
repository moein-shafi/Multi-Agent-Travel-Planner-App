import argparse
from crewai import Agent, Task, Crew, Process

DEFAULT_CITY = "Isfahan"
DEFAULT_COUNT = 3


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser("Simple multi-agent travel planner")
    p.add_argument("-c", "--city", default=DEFAULT_CITY, help="City to suggest attractions for")
    p.add_argument("-n", "--count", type=int, default=DEFAULT_COUNT, help="Number of attractions")
    p.add_argument("-q", "--quiet", action="store_true", help="Disable verbose crew output")
    return p.parse_args()

def main() -> None:
    args = parse_args()

    # Travel agent: suggests attractions for a city
    travel_agent = Agent(
        name="Travel Agent",
        role="Expert travel planner",
        description="Suggests popular attractions to visit in a specified city."
    )

    travel_task = Task(
        description=f"Suggest {args.count} popular attractions to visit in {args.city}.",
        expected_output=f"A list of {args.count} attractions in {args.city} with short descriptions.",
        agent=travel_agent
    )

    # Put agents and tasks together and run sequentially
    crew = Crew(
        agents=[travel_agent],
        tasks=[travel_task],
        process=Process.sequential,
        verbose=not args.quiet
    )

    try:
        result = crew.kickoff()
        print(result)
    except Exception as e:
        print("Error running crew:", e)

if __name__ == "__main__":
    main()