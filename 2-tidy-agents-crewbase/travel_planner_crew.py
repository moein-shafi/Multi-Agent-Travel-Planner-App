import os
import yaml
from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, crew, task    

from models import TravelItinerary
from custom_search_tool import CustomSearchTool


@CrewBase
class TravelPlannerCrew:
    """A crew for planning travel itineraries using real-time data"""
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # agents_config_path = os.path.join(base_dir, "config", "agents.yaml")
    # tasks_config_path = os.path.join(base_dir, "config", "tasks.yaml")

    agents_config_path = os.path.join(base_dir, "config", "agents-with-search-tools.yaml") # Updated to use agents config with search tool
    tasks_config_path = os.path.join(base_dir, "config", "tasks-with-search-tools.yaml") # Updated to use tasks config with search tool


    def __init__(self):
        with open(self.agents_config_path, 'r') as file:
            self.agents_data = yaml.safe_load(file)
            
        with open(self.tasks_config_path, 'r') as file:
            self.tasks_data = yaml.safe_load(file)

        # Initialize the custom search tool    
        self.search_tool = CustomSearchTool()

    @agent
    def researcher(self) -> Agent:
        """Creates a researcher agent"""
        return Agent(
            config=self.agents_data["researcher"],
            tools=[self.search_tool]  # Provide the search tool to the researcher agent
        )

    @agent
    def planner(self) -> Agent:
        """Creates a planner agent"""
        return Agent(
            config=self.agents_data["planner"]
        )

    @task
    def research_task(self) -> Task:
        """Creates a research task"""
        return Task(
            config=self.tasks_data["research_task"],
            agent=self.researcher()
        )

    @task
    def planning_task(self) -> Task:
        """Creates a planning task with full Pydantic validation"""
        return Task(
            config=self.tasks_data["planning_task"],
            agent=self.planner(),
            context=[self.research_task()],
            output_pydantic=TravelItinerary  # Comprehensive Pydantic validation
            # output_json=TravelItinerary  # Structured output as JSON-compatible dictionary
        )

    @crew
    def travel_crew(self) -> Crew:
        """Creates the travel planning crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential
        )    

