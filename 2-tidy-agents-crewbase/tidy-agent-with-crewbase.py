from travel_planner_crew import TravelPlannerCrew

def main() -> None:
    # Create an instance of our CrewBase class
    travel_planner = TravelPlannerCrew()

    # Access the crew method we decorated with @crew
    crew = travel_planner.travel_crew()

    # Define the input variables
    city = "Isfahan"
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
    print("Final Itinerary:")
    print(result)

    # Extract raw output
    raw_output = result.raw

    # Print the raw output
    print("\nRaw Output:")
    print(raw_output)

    # Extract Pydantic output
    pydantic_output = result.pydantic

    # Work with Pydantic output (if available)
    if pydantic_output:
        print(f"City: {pydantic_output.city}")
        print(f"Days: {pydantic_output.days}")
        print(f"First day attractions: {[a.name for a in pydantic_output.daily_plans[0].attractions]}")

        if pydantic_output.daily_plans[0].meal_suggestions:
            print(f"Meal suggestions for Day 1: {pydantic_output.daily_plans[0].meal_suggestions}")

        if pydantic_output.overall_tips:
            print(f"Overall Travel Tips: {pydantic_output.overall_tips}")

    json_output = result.json_dict
    if json_output:
        print("\nJSON Output:")
        print(json_output)



if __name__ == "__main__":
    main()