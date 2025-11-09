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
    travel_agent = Agent(
        name="Travel Agent",
        role="Expert travel planner",
        description="Suggests popular attractions to visit in a specified city."
    )

    travel_task = Task(
        description="Suggest {num_attractions} popular attractions to visit in {city}.",
        expected_output="A list of {num_attractions} attractions in {city} with short descriptions.",
        agent=travel_agent
    )

    # Set up inputs for the task
    inputs = {
        "city": args.city,
        "num_attractions": args.count
    }
    
    # Put agents and tasks together and run sequentially
    crew = Crew(
        agents=[travel_agent],
        tasks=[travel_task],
        process=Process.sequential,
        verbose=not args.quiet
    )

    try:
        result = crew.kickoff(inputs=inputs)
        print(result)
    except Exception as e:
        print("Error running crew:", e)

if __name__ == "__main__":
    main()