import argparse
import os
import yaml

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

    # Determine the base directory of the current file
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the agents configuration file
    agents_config_path = os.path.join(base_dir, "config", "agents.yaml")

    # Construct the path to the tasks configuration file
    tasks_config_path = os.path.join(base_dir, "config", "tasks.yaml")

    # Open and load the agents configuration file
    with open(agents_config_path, 'r') as file:
        agents_data = yaml.safe_load(file)

    # Open and load the tasks configuration file
    with open(tasks_config_path, 'r') as file:
        tasks_data = yaml.safe_load(file)

    # Create agents using the loaded configurations
    researcher = Agent(
        config=agents_data["researcher"]
    )

    planner = Agent(
        config=agents_data["planner"]
    )

    # Create tasks using the loaded configurations
    research_task = Task(
        config=tasks_data["research_task"],
        agent=researcher
    )

    planning_task = Task(
        config=tasks_data["planning_task"],
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