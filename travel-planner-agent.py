from typing import List
import argparse
from crewai import Agent, Task, Crew, Process

DEFAULT_CITY = "New York"
DEFAULT_COUNT = 3

def create_agent(role: str, goal: str, backstory: str) -> Agent:
    """Create and return an Agent instance."""
    return Agent(role=role, goal=goal, backstory=backstory)

def create_task(city: str, count: int, agent: Agent) -> Task:
    """Create a Task for suggesting attractions."""
    description = f"Suggest {count} popular attractions to visit in {city}."
    expected = f"A list of {count} popular attractions in {city} with brief descriptions."
    return Task(description=description, expected_output=expected, agent=agent)

def build_crew(agents: List[Agent], tasks: List[Task], verbose: bool = True) -> Crew:
    """Assemble and return a Crew."""
    return Crew(agents=agents, tasks=tasks, process=Process.sequential, verbose=verbose)

def run_crew(crew: Crew) -> str:
    """Run the crew and return the result as string. Exceptions are propagated."""
    return crew.kickoff()

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Multi-agent travel planner")
    p.add_argument("--city", "-c", default=DEFAULT_CITY, help="City to suggest attractions for")
    p.add_argument("--count", "-n", type=int, default=DEFAULT_COUNT, help="Number of attractions to suggest")
    p.add_argument("--quiet", "-q", action="store_true", help="Disable verbose crew output")
    return p.parse_args()

def main() -> None:
    args = parse_args()

    travel_agent = create_agent(
        role="Travel Agent",
        goal="Help users plan their trips",
        backstory="You are an experienced travel agent who loves helping people discover new places."
    )

    planning_task = create_task(city=args.city, count=args.count, agent=travel_agent)

    crew = build_crew(agents=[travel_agent], tasks=[planning_task], verbose=not args.quiet)

    try:
        result = run_crew(crew)
        print(result)
    except Exception as e:
        print(f"Error while running crew: {e}")

if __name__ == "__main__":
    main()