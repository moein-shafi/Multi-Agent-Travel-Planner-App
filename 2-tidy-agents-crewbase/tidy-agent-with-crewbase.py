from travel_planner_crew import TravelPlannerCrew

def main() -> None:
    # Create an instance of our CrewBase class
    travel_planner = TravelPlannerCrew()

    # Access the crew method we decorated with @crew
    crew = travel_planner.travel_crew()

    # Define the input variables
    city = "Cape Town"
    days = 2
    attractions_per_day = 2
    total_attractions = days * attractions_per_day

    # Build a dictionary using the variables
    inputs = {
        "city": city,
        "days": days,
        "attractions_per_day": attractions_per_day,
        "total_attractions": total_attractions
    }

    # Run the crew with inputs
    result = crew.kickoff(inputs=inputs)


if __name__ == "__main__":
    main()