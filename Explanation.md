# Introduction Section

Here we will explore the foundational concepts of `CrewAI`, focusing on `agents`, `tasks`, and `crews`. 

By the end of this part, you will:
 
- Understand how to create a simple agent,
- Define a task for it, 
- Assemble these components into a crew, 
- And Execute the crew to achieve a specific outcome. 

This part sets the stage for more advanced topics in subsequent parts, so let's dive in and start building your understanding of `CrewAI`.

## Key Concepts: What Are Agents, Tasks, and Crews?

An `agent`, in the context of artificial intelligence, is an autonomous entity that can perceive its environment, make decisions, and take actions to achieve specific goals. Unlike a simple chat model that merely responds to prompts, an agent has persistence, purpose, and the ability to take initiative based on its defined objectives. Agents can maintain context over time and operate with a degree of autonomy.

`CrewAI` builds on this concept by <u>providing a framework designed to orchestrate role-playing autonomous AI agents. It allows you to create a team of specialized AI agents that work together to accomplish complex tasks through collaboration</u>.

The main components of CrewAI are:

- `Agent`: A virtual entity designed to perform specific roles and achieve certain goals. Think of an agent as a digital assistant with a defined purpose, much like a travel agent who helps plan trips.

- `Task`: An action or a set of actions that an agent can perform. It includes a description and an expected output, similar to a to-do list item that needs completion.

- `Crew`: A collection of agents and tasks working together to accomplish a process. Imagine a team of specialists collaborating to complete a project.

These components form the backbone of CrewAI, enabling complex workflows to be managed efficiently.


## Installing CrewAI

To use CrewAI in your own Python environment, you can install it using pip:
```bash
pip install crewai
```

## Setting Up Your OpenAI API Key

CrewAI works with various language models, but in this course, we'll focus on using OpenAI models due to their robust performance and reliability.

```bash

# For Linux/Mac
export OPENAI_API_KEY=your_api_key_here

# For Windows (Command Prompt)
set OPENAI_API_KEY=your_api_key_here

# For Windows (PowerShell)
$env:OPENAI_API_KEY="your_api_key_here"

```

CrewAI will automatically detect and use this environment variable when you run your code, so there's no need to explicitly set it in your Python scripts.


## Setting Your Language Model


CrewAI allows you to specify which language model to use for your agents. You can configure your preferred model by setting an environment variable.

If you're using CrewAI in your own environment, you can set the model using the `OPENAI_API_MODEL` environment variable:

```Bash
# For Linux/Mac
export OPENAI_API_MODEL=gpt-4o-mini

# For Windows (Command Prompt)
set OPENAI_API_MODEL=gpt-4o-mini

# For Windows (PowerShell)
$env:OPENAI_API_MODEL="gpt-4o-mini"

```

CrewAI will automatically use the specified model for all agents unless you explicitly override it when creating an agent. This gives you flexibility to use different models for different agents based on their complexity and requirements.



# 1- Creating a Simple Agent

Now that we understand the key concepts and have our environment set up, let's start by creating a simple agent using the CrewAI library. In the code example below, we define a travel agent with specific attributes that shape its behavior.

```Python
from crewai import Agent

# Define a basic agent
travel_agent = Agent(
    role='Travel Agent',
    goal='Help users plan their trips',
    backstory='You are an experienced travel agent who loves helping people discover new places.'
)
```

Let's break down these parameters:

- `role`: Defines the agent's professional identity and function. This helps the underlying language model understand what expertise to simulate.
- `goal`: Specifies the agent's primary objective, guiding its decision-making process.
- `backstory`: Provides character depth and context, influencing how the agent "thinks" and responds.

Behind the scenes, CrewAI uses these parameters to construct a rich prompt that guides the language model's behavior. The role, goal, and backstory are incorporated into the system prompt sent to the model, effectively instructing it to embody this specific persona when generating responses. This technique, known as role-playing prompting, helps the model generate more focused and contextually appropriate outputs.



## Defining a Specific Task
A task represents a specific action or objective that an agent needs to complete. Tasks in CrewAI are structured with clear parameters that define what needs to be done and what output is expected.

```Python
from crewai import Task

# Define a task for the agent
planning_task = Task(
    description='Suggest 3 popular attractions to visit in New York.',
    expected_output='A list of 3 popular attractions in New York with brief descriptions.',
    agent=travel_agent
)
```

Here's what each parameter does:

- `description`: Provides detailed instructions about what the task involves. This forms the core prompt that will be sent to the language model.
- `expected_output`: Specifies the format and content of the desired result, helping the agent structure its response appropriately.
- `agent`: Associates the task with a specific agent who will be responsible for completing it.

When a task is executed, CrewAI constructs a comprehensive prompt that includes the agent's role, goal, and backstory, along with the task description and expected output format. This prompt is then sent to the language model, which generates a response based on this context. The model essentially "acts" as the defined agent while addressing the specific task requirements.

Tasks support additional parameters that we'll explore in later lessons as we build more complex agent workflows.




## Assembling a Simple Crew
With our agent and task defined, we can now assemble them into a crew. A crew is a structured group of agents and tasks that work together to complete a process.

```Python
from crewai import Crew, Process

# Assemble the crew
crew = Crew(
    agents=[travel_agent],
    tasks=[planning_task],
    process=Process.sequential,
    verbose=True
)
```

In this example, we're creating a simple crew with just one agent and one task, but CrewAI is designed to handle multiple agents and tasks working together. The parameters we're using are:

- `agents`: A list of all agents that will be part of the crew. In complex scenarios, this could include several specialized agents with different roles.
- `tasks`: A list of all tasks to be performed. In more sophisticated workflows, you might have numerous interconnected tasks.
- `process`: Defines how tasks are executed within the crew. CrewAI supports several process types:
    - `Process.sequential`: Tasks are executed one after another in order.
    - `Process.hierarchical`: Tasks are organized in a tree structure, with parent tasks delegating to child tasks.
    - `Process.parallel`: Multiple tasks are executed simultaneously.
- `verbose`: A boolean parameter that controls the level of output during execution. When set to `True`, CrewAI will display detailed logs showing the agent's thought process, task progression, and intermediate steps.


For our simple travel planning example, a sequential process works well. In more complex scenarios—like a research project requiring data collection, analysis, and report writing by different specialized agents—you might use a hierarchical or parallel process to optimize the workflow.


## Running the Crew and Observing Results

Once we've assembled our crew with the appropriate agents and tasks, we can execute it to see the system in action. The execution process is straightforward:

```Python
# Run the crew
result = crew.kickoff()

# Display the final output
print(result)
```

When you call the `kickoff()` method, CrewAI initiates the workflow according to the specified process type. For our sequential process, it will:

1. Take the first task in the list
1. Send it to the assigned agent (our travel agent)
1. The agent processes the task using the underlying language model
1. The result is captured and potentially passed to subsequent tasks (if there were any)
1. Finally, the output of the last task is returned as the result

Since we set `verbose=True` when creating our crew, you'll see detailed logs during execution. These logs show the agent's "thought process" and can include the task being processed, the agent's reasoning, and intermediate steps in the agent's work. These logs can be valuable for debugging and understanding how the agent approaches the task, but they are also verbose.

If you're only interested in the final output, you can simply capture the result returned by `kickoff()` and use it as needed. The final output will be a text response containing the travel agent's suggestions for popular attractions in New York, formatted according to the expected output we defined in the task:

```md
1. **Statue of Liberty**: An iconic symbol of freedom and democracy, the Statue of Liberty stands on Liberty Island in New York Harbor. Visitors can take a ferry to the island, explore the museum, and even climb to the crown for breathtaking views of the Manhattan skyline and the surrounding waters.

2. **Central Park**: This expansive green oasis in the heart of Manhattan offers a perfect escape from the city's hustle and bustle. Spanning over 840 acres, Central Park features picturesque walking paths, serene lakes, and recreational areas. Visitors can enjoy activities such as boating, biking, or simply relaxing on the Great Lawn. The park also hosts numerous landmarks, including Bethesda Terrace and the Central Park Zoo.

3. **Times Square**: Known as "The Crossroads of the World," Times Square is a vibrant commercial and entertainment hub famous for its dazzling neon lights, billboards, and bustling atmosphere. Visitors can experience street performances, shop at flagship stores, and dine at a variety of restaurants. The area is also home to Broadway theaters, where visitors can catch world-class productions and musicals.
```

This simple example demonstrates the core workflow of CrewAI: defining agents with specific roles, assigning them tasks, organizing these components into a crew, and executing the workflow to achieve your desired outcome.


## Creating Flexible Tasks with Placeholders

Placeholders are a powerful feature in CrewAI that allows tasks to be more flexible and adaptable. They act as variables within task descriptions and expected outputs, enabling you to define tasks that can change based on different inputs. This means you can create a single task template that can be reused in various scenarios by simply altering the input values. For example, instead of hardcoding a city name in a task, you can use a placeholder like `{city}`. This makes your tasks dynamic and reusable, allowing agents to handle a wider range of requests without needing to redefine tasks for each specific case.

Let's break down a code example to see how placeholders are used in practice. We start by defining a travel agent and a task with placeholders in the description and expected output.

```python
from crewai import Agent, Task, Crew, Process

# Define a basic agent
travel_agent = Agent(
    role='Travel Agent',
    goal='Help users plan their trips',
    backstory='You are an experienced travel agent who loves helping people discover new places.'
)

# Define a task with placeholders
planning_task = Task(
    description='Suggest {num_attractions} popular attractions to visit in {city}.',
    expected_output='A list of {num_attractions} popular attractions in {city} with brief descriptions.',
    agent=travel_agent
)
```

In this code, the `description` and `expected_output` fields of the `Task` class use placeholders `{num_attractions}` and `{city}`. These placeholders will be replaced with actual values when the task is executed, allowing the task to adapt to different input scenarios.

### Setting Up Dynamic Inputs

To utilize the placeholders effectively, we need to set up dynamic inputs that will be used during task execution. This involves specifying the values for the placeholders when the crew is run.


```python
# Set up inputs for the task
inputs = {
    "city": "San Diego",
    "num_attractions": 3
}
```

Here, we define a dictionary inputs with keys corresponding to the placeholders in the task. The values assigned to these keys will replace the placeholders during execution, allowing the task to be customized for different cities and numbers of attractions.


### Executing the Crew with Flexible Tasks

With the task and inputs defined, we can now execute the crew and observe how the placeholders are utilized during execution.



```python
# Assemble the crew
crew = Crew(
    agents=[travel_agent],
    tasks=[planning_task],
    process=Process.sequential
)

# Execute the crew with the specified inputs
result = crew.kickoff(inputs=inputs)

# Display the result
print(result)
```

When the `kickoff()` method is called, CrewAI processes the task by replacing the placeholders with the values from the `inputs` dictionary. The travel agent then uses these values to generate a response. The output will be a list of popular attractions in San Diego, formatted according to the expected output defined in the task.


# Building a Team of Specialized Travel Agents


In this lesson, we'll build a travel planning crew with specialized agents working together to create the perfect vacation itinerary:

- `Travel Researcher`: Our destination expert who hunts down the most interesting attractions, hidden gems, and must-see spots in any city.
```python
researcher = Agent(
    role="Travel Researcher",
    goal="Find the best attractions and activities",
    backstory="You are an expert at researching destinations and finding hidden gems."
)
```

- `Itinerary Planner`: Our organizational wizard who transforms a list of attractions into a coherent, efficient travel plan.


```python
planner = Agent(
    role="Itinerary Planner",
    goal="Create efficient and enjoyable travel plans",
    backstory="You excel at organizing activities into logical, time-efficient itineraries."
)
```

Together, these specialized agents combine their unique skills to deliver a comprehensive travel experience that neither could create alone.


## Creating a Workflow with Connected Tasks

Our travel planning crew will complete two interconnected tasks that flow naturally from one to the next:

- `Research Task`: The Travel Researcher will investigate attractions in the target city, providing rich descriptions of each location.


```python
research_task = Task(
    description="Research the top {total_attractions} attractions in {city} and provide brief descriptions.",
    expected_output="A list of {total_attractions} attractions in {city} with descriptions and why they're worth visiting.",
    agent=researcher
)
```


- `Planning Task`: The Itinerary Planner will take the researcher's findings and craft them into a day-by-day schedule.


```python
planning_task = Task(
    description="Create a {days}-day itinerary for {city} using only the researched attractions provided in the context.",
    expected_output="A detailed {days}-day schedule with exactly {attractions_per_day} attractions per day, including timing, transportation tips, and meal suggestions.",
    agent=planner,
    context=[research_task]
)
```


To connect these tasks, we use the `context=[research_task]` parameter when defining our planning task. This parameter tells CrewAI that the planning task needs information from the research task to do its job properly. Think of it as passing the research results directly to the planner so they have all the information they need to create a great itinerary.


## Assembling the Travel Planning Crew

With our travel experts defined and their tasks outlined, it's time to bring everything together into a cohesive travel planning team:

```python
crew = Crew(
    agents=[researcher, planner],
    tasks=[research_task, planning_task],
    process=Process.sequential
)
```


This crew setup creates our complete travel planning workflow:

- We provide a list of all our agents (`researcher` and `planner`) so the crew knows who's available to work

- We include all the tasks (`research_task` and `planning_task`) that need to be completed

- We set `process=Process.sequential` to ensure tasks run in order - this is crucial since our planning task depends on the results from the research task

The `Process.sequential` parameter is particularly important for our travel planning workflow. It tells CrewAI to execute tasks one after another in the order they appear in the tasks list. This ensures the Travel Researcher completes their work before the Itinerary Planner begins, maintaining our logical workflow from research to planning.


## Running the Crew and Analyzing Results

Once the crew is assembled, we can set up dynamic inputs and execute the crew to see how the agents work together. In our example, we calculate the total number of attractions based on the number of days and attractions per day, then pass these values as inputs to the crew:

```python
# Define input variables
city = "Barcelona"
days = 2
attractions_per_day = 2
total_attractions = days * attractions_per_day

# Build the dictionary using the variables
inputs = {
    "city": city,
    "days": days,
    "attractions_per_day": attractions_per_day,
    "total_attractions": total_attractions
}

# Run the crew with inputs
result = crew.kickoff(inputs=inputs)

# Display the result
print(result)
```


The output will be a detailed itinerary for a 2-day trip to Barcelona, including 4 researched attractions (2 per day), timing, transportation tips, and meal suggestions.



# Challenges of Hard-Coded Configurations


1. `Limited Maintainability`: When configurations are embedded in code, even small changes require modifying the source code, which can introduce bugs.

1. `Reduced Flexibility`: Hard-coded configurations make it difficult to adapt your agents and tasks for different scenarios without code changes.

1. `Poor Separation of Concerns`: Mixing business logic with configuration details violates the principle of separation of concerns, making code harder to understand and maintain.

1. `Collaboration Barriers`: When working in teams, non-technical stakeholders cannot easily review or modify configurations without developer assistance.

By externalizing configurations to YAML files, we can address these challenges and create more robust, adaptable CrewAI workflows that are easier to maintain as your projects grow in complexity.



## YAML Basics

YAML, which stands for "YAML Ain't Markup Language", is a human-readable data serialization format that is commonly used for configuration files. Its syntax is simple and intuitive, making it an excellent choice for defining configuration data. YAML uses indentation to represent structure, similar to Python, and supports complex data types such as lists and dictionaries. This makes it ideal for representing hierarchical data, such as the configurations of agents and tasks in CrewAI.

## Externalizing Agent Configurations

Now that we understand YAML basics, let's examine how to apply this format to externalize agent configurations in CrewAI. Consider the following agents.yaml file:

```YAML
researcher:
  role: "Travel Researcher"
  goal: "Find the best attractions, activities, and local cultural insights."
  backstory: "You are an expert at researching destinations, using the latest information from the web to uncover hidden gems and local customs."
  
planner:
  role: "Itinerary Planner"
  goal: "Create efficient and enjoyable travel plans"
  backstory: "You excel at organizing activities into logical, time-efficient itineraries."
```


In this file, we define two agents: a Travel Researcher and an Itinerary Planner. Each agent has a role, a goal, and a backstory. By using YAML, we can easily modify these attributes without altering the main codebase. This separation of concerns enhances the maintainability of our CrewAI projects.


## Externalizing Task Configurations


Next, let's look at how to externalize task configurations with a YAML file. Here is the `tasks.yaml` file:

```YAML
research_task:
  description: |
    Research the top {total_attractions} attractions in {city} and gather local customs and cultural insights.
  expected_output: "A combined list of {total_attractions} attraction(s) with detailed information and local cultural insights for {city}."
  
planning_task:
  description: |
    Create a {days}-day itinerary for {city} using only the researched attractions provided in the context.
    Include:
    1. A logical sequence {attractions_per_day} attractions for each day.
    2. Transportation recommendations between locations.
    3. Meal suggestions respecting local dining customs.
    4. Key cultural considerations for each activity.
  expected_output: "A detailed {days}-day schedule with exactly {attractions_per_day} attractions per day, including timing, transportation tips, meal suggestions, and cultural guidance."
```

In this file, we define two tasks: a research task and a planning task. Each task has a description and an expected output. Notice the pipe symbol (`|`) after the description key - this YAML feature preserves line breaks in the text that follows, allowing for multi-line descriptions that maintain their formatting.

The use of placeholders, such as `{total_attractions}`, `{city}`, `{days}`, and `{attractions_per_day}`, allows for dynamic input, making the tasks adaptable to different scenarios. By externalizing task configurations, we can easily update task details and dependencies without modifying the core code.



## Project Structure for YAML Configuration

Before diving into loading the configuration files, let's examine our project structure with externalized YAML configurations:

```Plain text
app/
│
├── config/             # Directory for all configuration files
│   ├── agents.yaml     # Agent configurations
│   └── tasks.yaml      # Task configurations
│
└── main.py             # Main application code
```

This structure separates our configuration data from our application code, making it easier to maintain and update. The `config` directory contains all YAML files, keeping our configurations organized in one place.

Now that we have our configurations in YAML files, let's integrate them into the CrewAI workflow.

## Loading YAML Configuration Files
First, we need to determine the base directory, locate our YAML files in the `config` directory, and load them safely:

```Python
import os
import yaml

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
```

This code performs three essential steps to safely load our YAML configuration files:

1. **Determines the base directory**: Finds the absolute path of the directory containing our script, ensuring we can locate configuration files regardless of where the script is executed from.

1. **Constructs file paths**: Builds the complete paths to our configuration files stored in the `config` subdirectory, maintaining proper file organization.

1. **Safely loads YAML content**: Uses PyYAML's `safe_load()` method to parse the YAML content into Python dictionaries, which protects against potentially malicious YAML content while converting the configuration data into usable Python objects.

## Creating Agents and Tasks from Configurations

With our configuration data now loaded into Python dictionaries, we can proceed to create our Agent and Tasks objects using the `config` parameter:

```Python
from crewai import Agent, Task

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
```
Notice how we pass the configuration data directly to the `config` parameter of the Agent and Task constructors. CrewAI will automatically map the YAML properties to the appropriate attributes of the objects.

## Building and Executing the Crew

Finally, we build the crew and execute the workflow, which should be familiar from previous lessons:

```Python
from crewai import Crew, Process

# Create a crew with the configured agents and tasks
crew = Crew(
    agents=[researcher, planner],
    tasks=[research_task, planning_task],
    process=Process.sequential
)

# Define the input variables
city = "Istanbul"
days = 2
attractions_per_day = 2
total_attractions = days * attractions_per_day

# Build the dictionary using the variables
inputs = {
    "city": city,
    "days": days,
    "attractions_per_day": attractions_per_day,
    "total_attractions": total_attractions
}

# Run the crew with inputs
result = crew.kickoff(inputs=inputs)

# Display the result
print(result)
```

The crew is created and executed as before, but now with agents and tasks that are configured through external YAML files. The `inputs` dictionary provides values for the placeholders in our task descriptions, making our workflow adaptable to different scenarios without code changes.



# 2- Tidy Agent Code with CrewBase 


In this lesson, we will focus on organizing and structuring agent code using CrewBase in CrewAI projects. The objective is to help you understand how tidy, well-organized code can enhance the efficiency and maintainability of your projects. By the end of this lesson, you will be able to create a travel planning crew using CrewAI, which will serve as a foundation for more complex integrations in future lessons.

Tidy and well-organized code is crucial in any software project, and CrewAI is no exception. It ensures that your code is easy to read, understand, and modify, which is essential for collaboration and long-term project success. Let's dive into the fundamentals of CrewBase and how it helps in structuring your CrewAI projects.

## Understanding CrewBase Fundamentals
CrewBase is a foundational component in CrewAI that helps you organize your code in a clean and efficient way. It provides a framework for grouping together agents, tasks, and crews so your project stays tidy and easy to manage. In CrewBase, you’ll see special symbols like @agent, @task, and @crew placed above certain functions—these are called decorators in Python. Decorators are a feature in Python that let you add extra behavior or meaning to functions or classes. In CrewBase, these decorators tell CrewAI which functions are responsible for creating agents, tasks, or crews, making your code more organized and easier to understand.

```python
from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class SimpleCrew:
    
    @agent
    def researcher(self) -> Agent:
        return Agent(
            role="Researcher",
            goal="Find accurate information",
            backstory="You are an expert at finding information quickly and accurately."
        )
    
    @task
    def research_task(self) -> Task:
        return Task(
            description="Research the given topic thoroughly",
            agent=self.researcher()
        )
    
    @crew
    def simple_crew(self) -> Crew:
        return Crew(
            agents=[self.researcher()],
            tasks=[self.research_task()],
            process=Process.sequential
        )
```

The @agent decorator is used to define agents, which are the building blocks of your CrewAI project. The @task decorator is used to define tasks, which are specific actions or processes that agents perform. Finally, the @crew decorator is used to define crews, which are collections of agents and tasks working together to achieve a common goal.

## Structuring a Travel Planner with CrewBase Class

Let's explore how to create a well-structured travel planner using CrewBase. We'll examine the TravelPlannerCrew class, which provides an organized framework for planning comprehensive travel itineraries while demonstrating best practices for code organization in CrewAI projects.

```python
import os
import yaml
from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class TravelPlannerCrew:
    """A crew for planning travel itineraries"""
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    agents_config_path = os.path.join(base_dir, "config", "agents.yaml")
    tasks_config_path = os.path.join(base_dir, "config", "tasks.yaml")
    
    def __init__(self):
        with open(self.agents_config_path, 'r') as file:
            self.agents_data = yaml.safe_load(file)
            
        with open(self.tasks_config_path, 'r') as file:
            self.tasks_data = yaml.safe_load(file)
```

The class uses configuration files, agents.yaml and tasks.yaml, to load data for agents and tasks. These configuration files allow you to separate the configuration data from the code, making it easier to manage and update. The TravelPlannerCrew class reads these files during initialization and uses the data to create agents and tasks.


## Tidy Agent Code with the @agent Decorator

The @agent decorator simplifies the creation of agents by providing a clear and concise way to define them. In the TravelPlannerCrew class, we define two agents: a researcher and a planner.

```python
@agent
def researcher(self) -> Agent:
    """Creates a researcher agent"""
    return Agent(
        config=self.agents_data["researcher"]
    )

@agent
def planner(self) -> Agent:
    """Creates a planner agent"""
    return Agent(
        config=self.agents_data["planner"]
    )
```

Each agent method is decorated with @agent, indicating that it creates an agent. The agent configuration is loaded from the agents.yaml file, which keeps the code clean and separates the configuration from the implementation. This approach makes it easy to modify agent properties without changing the code structure.



## Organizing Tasks with the @task Decorator

The @task decorator helps organize tasks in a clean and maintainable way. In our TravelPlannerCrew class, we define two tasks: a research task and a planning task.

```python
@task
def research_task(self) -> Task:
    """Creates a research task"""
    return Task(
        config=self.tasks_data["research_task"],
        agent=self.researcher()
    )

@task
def planning_task(self) -> Task:
    """Creates a planning task"""
    return Task(
        config=self.tasks_data["planning_task"],
        agent=self.planner(),
        context=[self.research_task()]
    )
```

The research_task method creates a task assigned to the researcher agent, while the planning_task method creates a task assigned to the planner agent.



## Creating a Crew with the @crew Decorator

The @crew decorator is used to define the crew, which brings together agents and tasks into a cohesive unit. In our TravelPlannerCrew class, we define a travel_crew method that creates the travel planning crew.

```python
@crew
def travel_crew(self) -> Crew:
    """Creates the travel planning crew"""
    return Crew(
        agents=self.agents,
        tasks=self.tasks,
        process=Process.sequential
    )
```

The travel_crew method creates a crew that includes all the defined agents and tasks, organizing them into a sequential process. The self.agents and self.tasks properties are automatically populated by CrewBase based on the methods decorated with @agent and @task, respectively.



## Using the Travel Planner Crew

Once the TravelPlannerCrew class is defined, using it is straightforward. The key is understanding how to instantiate the class and access the crew you've defined with the @crew decorator:

```python
from travel_planner_crew import TravelPlannerCrew

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
```

Notice how we first instantiate our TravelPlannerCrew class, then access the travel_crew() method which returns our fully configured Crew object. This is the power of the CrewBase pattern - all the agent and task creation happens behind the scenes when you call the crew method, giving you a clean interface to work with.


# Using Pydantic Models for Structured Output


Welcome back to the course Expanding CrewAI Capabilities and Integration. In our previous lesson, we explored how to organize and structure agent code using CrewBase in CrewAI projects. This lesson builds on that foundation by introducing you to the use of Pydantic models for structured, validated outputs. Structured outputs are crucial in ensuring that data is consistent, reliable, and easy to integrate with other systems. They help prevent errors and misinterpretations that can arise from unstructured data, thereby enhancing the overall robustness of your applications.

CrewAI enforces structured outputs by leveraging Pydantic models, which provide a framework for data validation and type checking. This ensures that the outputs from CrewAI tasks are not only integration-friendly but also adhere to the expected data formats, making your CrewAI projects more reliable and efficient. By the end of this lesson, you will understand how to leverage Pydantic models to enhance the robustness of your CrewAI projects, particularly in the context of travel itinerary planning.

## Installing and Setting Up Pydantic
Before we dive into using Pydantic, let's quickly cover how to install it. On your local setup, you can install Pydantic using pip with the following command:

```Bash
pip install pydantic
```

However, if you are working within the CodeSignal environment, you don't need to worry about installation, as Pydantic is pre-installed. This allows you to focus on learning and applying Pydantic without the hassle of setup.


## Defining the Desired Output Structure

To effectively create Pydantic models for our travel itinerary application, we first need to define a plan for our desired output structure. This ensures that the models align with the requirements and expectations of our application. Below is the expected structure of our output, which will guide the creation of our Pydantic models:

- Travel Itinerary: The overall plan for a trip
    - City: Name of the city to visit
    - Days: Number of days in the itinerary
    - Daily Plans: A list of plans for each day
        - Day Number: The specific day in the itinerary (e.g., 1 for the first day, 2 for the second day)
        - Attractions: A list of attractions to visit on this day
            - Name: Name of the attraction
            - Description: Brief description of the attraction
            - Category: Category like 'Museum', 'Historical Site', etc.
            - Estimated Duration: How long to spend here (e.g., '2 hours')
            - Address: Physical address, if available
        - Meal Suggestions: A list of suggested places to eat, if available
    - Overall Tips: General travel tips for this destination, if available

This structure outlines the key components of a travel itinerary, including the city to visit, the number of days, and detailed daily plans. Each daily plan consists of a list of attractions, each with specific details such as name, description, category, estimated duration, and address. Additionally, there are optional meal suggestions and overall travel tips. This organized structure will be enforced by our Pydantic models to ensure data integrity and consistency.

## Creating Pydantic Models for Travel Itineraries

Now, let's explore how to create Pydantic models for our travel itinerary application. Pydantic models are defined as Python classes that inherit from BaseModel. They provide type checking, default values, and field descriptions, which are crucial for ensuring data integrity.

Consider the following Pydantic models for a travel itinerary:

```python
from typing import List, Optional
from pydantic import BaseModel, Field

class Attraction(BaseModel):
    """Model for a tourist attraction"""
    name: str = Field(description="Name of the attraction")
    description: str = Field(description="Brief description of the attraction")
    category: str = Field(description="Category like 'Museum', 'Historical Site', etc.")
    estimated_duration: str = Field(description="How long to spend here (e.g., '2 hours')")
    address: Optional[str] = Field(description="Physical address", default=None)

class DailyPlan(BaseModel):
    """Model for a single day in the itinerary"""
    day_number: int = Field(description="Day number in the itinerary")
    attractions: List[Attraction] = Field(description="List of attractions to visit")
    meal_suggestions: Optional[List[str]] = Field(description="Suggested places to eat", default=None)

class TravelItinerary(BaseModel):
    """Model for a complete travel itinerary"""
    city: str = Field(description="City to visit")
    days: int = Field(description="Number of days in the itinerary")
    daily_plans: List[DailyPlan] = Field(description="Plan for each day")
    overall_tips: Optional[str] = Field(description="General travel tips for this destination", default=None)
```

These models define the structure of our data, ensuring that each field is of the expected type and providing default values where necessary. Lists, such as List[Attraction] and List[str], are used to represent collections of items, while Optional fields, like Optional[str] and Optional[List[str]], indicate that a field is not mandatory and can be None. The Field function allows us to add descriptions, which can be helpful for documentation and understanding the purpose of each field. For example, descriptions like "Name of the attraction" or "Suggested places to eat" provide clarity on what each field represents.

## Understanding CrewAI's Output Structuring Parameters
CrewAI provides two main parameters to structure and validate task outputs clearly and effectively:

- `output_json`: Accepts a Pydantic model defining the desired output structure. CrewAI validates and structures the raw output into a JSON-compatible Python dictionary, accessible through result.json_dict. This format is ideal when you need serialization or integration with other systems expecting JSON.

- `output_pydantic`: Also accepts a Pydantic model class but provides deeper validation, converting the output into a fully instantiated and validated Pydantic model instance. This instance is accessible via result.pydantic, offering direct, type-safe attribute access and comprehensive validation (including type checking, required fields, and custom validators).

Both parameters rely on Pydantic models to define output structure. The crucial difference lies in the resulting format: output_json yields a dictionary, while output_pydantic provides a fully instantiated and validated object.

## Integrating Pydantic Models into CrewAI Tasks
With Pydantic models defined, you can integrate them seamlessly into CrewAI tasks, ensuring structured, validated outputs.

In the TravelPlannerCrew class, use output_pydantic to produce validated model instances:

```python
from models import TravelItinerary

@task
def planning_task(self) -> Task:
    """Creates a planning task with full Pydantic validation"""
    return Task(
        config=self.tasks_data["planning_task"],
        agent=self.planner(),
        context=[self.research_task()],
        output_pydantic=TravelItinerary  # Comprehensive Pydantic validation
    )
```


This approach validates the task's output against the TravelItinerary model, providing type-safe and attribute-based access through result.pydantic.

Alternatively, to obtain outputs as dictionaries suitable for serialization or external systems, use output_json:

```python
@task
def planning_task(self) -> Task:
    """Creates a planning task with structured JSON output"""
    return Task(
        config=self.tasks_data["planning_task"],
        agent=self.planner(),
        context=[self.research_task()],
        output_json=TravelItinerary  # Structured output as JSON-compatible dictionary
    )
```

Here, CrewAI validates and structures the output following the TravelItinerary model's schema, providing easy dictionary access via result.json_dict.

Internally, CrewAI leverages these parameters by embedding explicit model-based formatting instructions into agent prompts. It instructs the LLM to structure outputs accordingly. If validation initially fails, CrewAI may retry with clearer instructions or raise exceptions, ensuring robust and predictable structured outputs.

## Running the Crew and Inspecting Structured Output
Let's see how these integrations work in practice by running the crew and inspecting the outputs:

```python
from travel_planner_crew import TravelPlannerCrew

# Create the crew
travel_planner = TravelPlannerCrew()

# Define the input variables
city = "Buenos Aires"
days = 2
attractions_per_day = 2
total_attractions = days * attractions_per_day

# Build the dictionary using the variables
inputs = {
    "city": city,
    "days": days,
    "attractions_per_day": attractions_per_day,
    "total_attractions": total_attractions
}

# Run the crew and get the result
result = travel_planner.travel_crew().kickoff(inputs=inputs)
```

## Examining Raw Output
The raw output is the complete, unstructured text response generated by the agent. It's the most basic form of output and is always available, regardless of the output parameters specified. This output is useful for seeing exactly what the agent produced without any additional processing or formatting:

```python
# Extract raw output
raw_output = result.raw

# Print the raw output
print(raw_output)
```


Here's a simplified example of what the raw output might look like:

```Plain text
{
  "city": "Buenos Aires",
  "days": 2,
  "daily_plans": [
    {
      "day_number": 1,
      "attractions": [
        {
          "name": "The Obelisco",
          "description": "This iconic monument...",
          ...
        },
        ...
      ],
      "meal_suggestions": [
        "Lunch at a nearby café...",
        ...
      ]
    },
    ...
  ],
  "overall_tips": "Experience public gatherings at The Obelisco..."
}
```

The raw output provides a full view of the agent's response, which can be quite detailed and is useful for understanding the context and content generated by the agent.

## Working with JSON Output
The JSON output is a structured version of the agent's response. When you specify the output_json parameter in your task, CrewAI formats the output into a JSON-compatible dictionary. This makes it easier to work with programmatically, especially if you need to integrate with other systems or serialize the data:

```python
# Extract JSON output
json_output = result.json_dict

# Print JSON output (if available)
if json_output:
    print(json_output)
```

Here's a trimmed version of the JSON output:

```Plain text
{'city': 'Buenos Aires', 'days': 2, 'daily_plans': [{'day_number': 1, 'attractions': [{'name': 'La Boca', 'description': 'Vibrant neighborhood', 'category': 'Cultural', 'estimated_duration': '2-3 hours', 'address': 'Caminito, Buenos Aires'}, ...], 'meal_suggestions': ['Argentine asado', '...']}, ...], 'overall_tips': 'Engage with performers...'}
```

The JSON output is structured and easy to parse, making it suitable for further processing or integration with other systems. Remember, this output will only be available if you set the output_json parameter in your task.

## Leveraging Pydantic Objects
The Pydantic output is the most advanced form of output. When you use the output_pydantic parameter in your task, CrewAI converts the response into a fully validated Pydantic object. This allows you to interact with the data in a more intuitive and type-safe manner, ensuring data integrity and making it easier to access specific attributes:

```python
# Extract Pydantic output
pydantic_output = result.pydantic

# Work with Pydantic output (if available)
if pydantic_output:
    print(f"City: {pydantic_output.city}")
    print(f"Days: {pydantic_output.days}")
    print(f"First day attractions: {[a.name for a in pydantic_output.daily_plans[0].attractions]}")
```

Here's an example of what the Pydantic output might look like:

```Plain text
City: Buenos Aires
Days: 2
First day attractions: ['Recoleta Cemetery', 'Teatro Colón']
```

The Pydantic output allows you to access the data as attributes of an object, making it straightforward to work with complex nested data structures. This approach ensures that the data adheres to the expected format and types, providing a reliable way to handle the output in your application. Remember, this output will only be available if you set the output_pydantic parameter in your task.




# Creating and Integrating a Custom Search Tool

In our previous lessons, you learned how to organize agent code using CrewBase and how to use Pydantic models for structured outputs. These foundational skills are crucial as we move forward to enhance the functionality of our CrewAI projects.

One of the most powerful aspects of CrewAI is the ability to equip agents with tools that extend their capabilities beyond just reasoning. Tools allow agents to interact with external systems, retrieve information, and perform actions in the real world. Search tools are particularly valuable as they enable agents to access up-to-date information from the web, making their responses more accurate and relevant.

There are many search tools that you can easily integrate into your crew, but most of them require you to set up a payment method and use API keys. In this lesson, we will learn how to create and integrate our own free search tool using DuckDuckGo. We'll cover not only how to create custom tools but also how agents are given access to these tools within the CrewAI framework.

By the end of this lesson, you will understand the process of creating custom tools, specifically a search tool that doesn't require API keys, and how to properly configure agents to utilize these tools in their decision-making processes. This knowledge will empower you to extend your CrewAI projects with custom capabilities while avoiding unnecessary costs.

## Installing Additional Libraries

Before we dive into building our custom search tool, let's ensure our environment is ready. For this lesson, we will use two key libraries: LangChain Community and DuckDuckGoSearch. These libraries will enable us to perform web searches and integrate them into our CrewAI project.

To install these libraries on your local machine, you can use the following pip commands:

```Bash
# Install langchain-community which provides the DuckDuckGoSearchResults tool
pip install langchain-community

# Install duckduckgo-search which enables web searches without requiring API keys
pip install duckduckgo-search
```

Once again, if you are working within the CodeSignal environment, you don't need to worry about installation, as these libraries are pre-installed.

## Building the Custom Search Tool

Now, let's build our custom search tool. We will create a new tool by subclassing BaseTool from the crewai.tools module. This custom tool will use DuckDuckGoSearchResults from the langchain_community.tools module to perform web searches.

Here's how you can define the CustomSearchTool:

```Python
from crewai.tools import BaseTool
from langchain_community.tools import DuckDuckGoSearchResults

# Create a custom tool by subclassing BaseTool
class CustomSearchTool(BaseTool):
    # Define the tool's name that will be displayed to the agent
    name: str = "DuckDuckGo Search Tool"
    # Provide a description that helps the agent understand when to use this tool
    description: str = "Search the web using DuckDuckGo (free)."

    def _run(self, query: str) -> str:
        # Instantiate the underlying LangChain tool
        ddg_tool = DuckDuckGoSearchResults()
        # Use the tool to perform the search
        response = ddg_tool.invoke(query)
        # Return the search results from DuckDuckGo to the agent
        return response
```

In this code, we define a class CustomSearchTool that inherits from BaseTool. The _run method is where the search logic resides. It uses DuckDuckGoSearchResults to perform a web search based on the query provided. The result is then returned as a response.


## Integrating the Custom Search Tool into the Travel Planner Crew

With our custom search tool ready, the next step is to integrate it into the travel planner crew. This involves adding the tool within the crew's initialization and ensuring it is accessible to the relevant agents and tasks.

In the TravelPlannerCrew class, we initialize the CustomSearchTool and integrate it with the researcher agent:

```Python
from crewai import Agent
from crewai.project import CrewBase, agent
from custom_search_tool import CustomSearchTool

@CrewBase
class TravelPlannerCrew:
    """A crew for planning travel itineraries using real-time data"""
    
    # Configuration file paths...
    
    def __init__(self):
        # Code for loading agent and task configurations...
        
        # Initialize the custom search tool    
        self.search_tool = CustomSearchTool()

    @agent
    def researcher(self) -> Agent:
        """Creates a researcher agent"""
        return Agent(
            config=self.agents_data["researcher"],
            tools=[self.search_tool]  # Provide the search tool to the researcher agent
        )
```

Here, the CustomSearchTool is instantiated and assigned to self.search_tool. The researcher agent is then created with access to this tool, allowing it to perform web searches as part of its tasks.



## Updating Agent and Task Configurations

With our custom search tool ready, we need to update our agent and task configurations to fully leverage this new capability. The agent configuration should emphasize the use of web search tools, while the task configuration should explicitly instruct the agent to perform searches.

Let's update the researcher agent configuration in agents.yaml:

```YAML
researcher:
  role: "Travel Researcher"
  goal: "Find the best attractions, activities, and local cultural insights using real-time web data"
  backstory: "You are an expert at researching destinations, using the latest information from the web to uncover hidden gems and local customs."
```

This configuration emphasizes that the researcher uses "real-time web data" and is an expert at "using the latest information from the web." These phrases signal to the agent that it should utilize the search tool we've provided.

Similarly, we need to update the research task in tasks.yaml to explicitly instruct the agent to perform web searches:

```YAML
research_task:
  description: |
    Research the top {total_attractions} attractions in {city} and gather local customs and cultural insights.
    1. Search for popular attractions and local customs in {city}.
    2. Compile the information into structured data.
  expected_output: "A combined list of {total_attractions} attraction(s) with detailed information and local cultural insights for {city}."
```

The task description now includes a clear instruction to "Search for popular attractions and local customs," which encourages the agent to use the search tool we've provided.

By aligning our agent and task configurations with the capabilities of our custom search tool, we ensure that the agent understands when and how to use the tool effectively during the execution of its tasks.

## Observing the Tool in Action

When you run your crew with the custom search tool, you can observe how the agent uses it to gather information. Let's see what happens when we run our travel planner crew for a trip to Dubai with verbose mode enabled:

```Plain text
🚀 Crew: crew
└── 📋 Task: d1f30b34-c44e-43de-bda8-5022fc92495c
       Status: Executing Task...
    └── 🤖 Agent: Travel Researcher
            Status: In Progress
        └── 🔧 Used DuckDuckGo Search Tool (1)

# Agent: Travel Researcher
## Thought: I need to search for popular attractions and local customs in Dubai to gather detailed information.
## Using tool: DuckDuckGo Search Tool
## Tool Input: 
"{\"query\": \"top attractions in Dubai and local customs cultural insights\"}"
## Tool Output: 
snippet: Remember to dress modestly, be respectful of religious sites, and observe local customs and etiquette. 
Engage with the local culture through food,  markets, and festivals, and be open to learning from the Emirati community. 
By doing so, you'll gain a deeper understanding and appreciation  for Dubai's rich cultural heritage., title: Dubai Cultural Guide: 
Understanding Local Traditions and Customs, link: 
https://www.consultancy-emirates.com/visit-dubai/cultural-insights/dubai-cultural-guide-understanding-local-traditions-and-customs/, ...
```

In this output, you can see:

1. The agent identifies the need to search for information about Dubai attractions and customs
1. It selects the DuckDuckGo Search Tool we provided
1. It formulates a search query combining both attractions and cultural insights
1. The tool returns real search results with snippets from various websites about Dubai's culture, attractions, and customs

This demonstrates how our custom search tool empowers the agent with the ability to access up-to-date information from the web. The agent can now use these search results to compile a more accurate and comprehensive travel plan for Dubai, including both popular attractions and important cultural insights that travelers should be aware of.



# Leveraging CrewAI's Built-in Tools for Web Scraping

Web scraping is a powerful technique that allows your AI agents to autonomously gather and process data from websites. By integrating web scraping, you can enhance the data-driven decision-making capabilities of your AI projects, making them more dynamic and responsive to real-world information. This lesson will guide you through the process of setting up and using CrewAI's ScrapeWebsiteTool to achieve this.

## Setting Up CrewAI Tools

To use CrewAI's built-in web scraping capabilities, you'll need to install the appropriate libraries on your local machine. The primary package you need is crewai-tools, which contains the ScrapeWebsiteTool and other utilities for enhancing your CrewAI agents:

```Bash
pip install crewai-tools
```

The crewai-tools package provides a collection of ready-to-use tools that extend the functionality of your CrewAI agents, including web scraping, search capabilities, and more. These tools are designed to work seamlessly with the core CrewAI framework, allowing your agents to interact with external data sources efficiently. If you're working within the CodeSignal environment for this course, you don't need to worry about this installation step, as all the necessary libraries are already pre-installed and ready to use.

## Overview of CrewAI's Built-in ScrapeWebsiteTool

CrewAI provides a built-in tool called ScrapeWebsiteTool designed to gather data from websites. This tool simplifies the process of web scraping by providing a straightforward interface for extracting information. The ScrapeWebsiteTool can be used to collect data such as text, images, and links from web pages, making it a versatile addition to your AI toolkit.

Here's a simple code snippet demonstrating how to use the ScrapeWebsiteTool:

```Python
from crewai_tools import ScrapeWebsiteTool

# Initialize the scraping tool
scrape_tool = ScrapeWebsiteTool()

# Use the tool to scrape data from a website
data = scrape_tool.scrape("https://example.com")

# Print the scraped data
print(data)
```

This snippet shows how to initialize the ScrapeWebsiteTool and use it to scrape data from a website. The scrape method takes a URL as input and returns the extracted data, which can then be processed or analyzed further.

## Integrating the ScrapeWebsiteTool

CrewAI provides a built-in tool called ScrapeWebsiteTool designed to gather data from websites. This tool simplifies the process of web scraping by providing a straightforward interface for extracting information. The ScrapeWebsiteTool can be used to collect data such as text, images, and links from web pages, making it a versatile addition to your AI toolkit.

Similar to how we integrated our custom search tool earlier, adding the ScrapeWebsiteTool to our crew follows the same pattern. Let's add it to our existing TravelPlannerCrew class:

```Python
from crewai import Agent
from crewai.project import CrewBase, agent
from crewai_tools import ScrapeWebsiteTool
from custom_search_tool import CustomSearchTool

@CrewBase
class TravelPlannerCrew:
    """A crew for planning travel itineraries using real-time data"""
    
    # Configuration file paths...
    
    def __init__(self):
        # Code for loading agent and task configurations...
        
        # Initialize the custom search tool    
        self.search_tool = CustomSearchTool()
        # Initialize the web scraping tool
        self.scrape_tool = ScrapeWebsiteTool()

    @agent
    def researcher(self) -> Agent:
        """Creates a researcher agent that gathers attraction data and local cultural insights"""
        return Agent(
            config=self.agents_data["researcher"],
            tools=[self.search_tool, self.scrape_tool]  # Provide the scraping tool to the researcher agent
        )
```

Just as we did with our search tool, we instantiate the ScrapeWebsiteTool and add it to the researcher agent's toolkit. This gives our agent the ability to not only search for information but also extract detailed data directly from websites.

## Updating Task Configurations for Web Scraping

To effectively utilize the ScrapeWebsiteTool, we need to update our task configurations to explicitly instruct agents to perform web scraping. Let's modify the research_task in the tasks.yaml file to include web scraping steps:

```YAML
research_task:
  description: |
    Research the top {total_attractions} attraction(s) in {city} and gather local customs and cultural insights.
    1. Search for popular attractions and local customs in {city}.
    2. Scrape official websites and travel advisories for details such as opening hours, addresses, and cultural tips.
    3. Compile the information into structured data.
  expected_output: "A combined list of {total_attractions} attraction(s) with detailed information and local cultural insights for {city}."
In this updated configuration, we've added a specific step (step 2) that instructs the agent to scrape official websites for detailed information. This explicit instruction ensures that the agent will utilize the ScrapeWebsiteTool we provided earlier.
```

The key to effective web scraping with CrewAI is to be specific about:

- What websites to target (official attraction sites, travel advisories)
- What information to extract (opening hours, addresses, cultural tips)
- How to process the scraped data (compile into structured format)

By including these details in your task description, you guide the agent to make appropriate use of the scraping tool within its workflow.


## Observing the ScrapeWebsiteTool in Action

When you run your crew with the ScrapeWebsiteTool, you can observe how the agent uses it to extract detailed information from websites. Let's see what happens when we run our travel planner crew for a trip to Chicago with verbose mode enabled:

```Plain text
🚀 Crew: crew
└── 📋 Task: d87f5b60-2499-447f-8d25-06b937287ca7
       Status: Executing Task...
    └── 🤖 Agent: Travel Researcher
            Status: In Progress
        ├── 🔧 Used DuckDuckGo Search Tool (1)
        └── 🔧 Used Read website content (1)

# Agent: Travel Researcher
## Thought: I need to gather detailed information about attractions in Chicago from official websites.
## Using tool: Read website content
## Tool Input: 
"{\"website_url\": \"https://www.timeout.com/chicago/things-to-do/chicago-attractions-the-best-sights-and-attractions-in-chicago\"}"
## Tool Output: 
40 Best Chicago Attractions That You Have to Visit in 2025 Go to the content Go to the footer No thanks Subscribe 🙌 Awesome, 
you're subscribed! Thanks for subscribing! Look out for your first newsletter in your inbox soon! The best of Chicago straight 
to your inbox We help you navigate a myriad of possibilities. Sign up for our newsletter for the best of the city. Enter email 
address Déjà vu! We already have this email. Try another? By entering your email address you agree to our Terms of Use and...
```

In this output, you can see:

1. The agent identifies the need to gather detailed information about Chicago attractions from official websites.
1. It selects the Read website content tool, which is part of the ScrapeWebsiteTool.
1. It provides the URL of a website containing information about Chicago attractions.
1. The tool returns the content of the webpage, which includes a list of attractions and additional information.

This demonstrates how the ScrapeWebsiteTool empowers the agent to extract specific data directly from websites, enabling it to compile a more accurate and comprehensive travel plan for Chicago. The agent can now use this detailed information to enhance the travel itinerary with up-to-date and relevant insights.


# 3- Creating a Travel Planner RESTful API with Flask

## Introduction and Lesson Overview
Welcome to the first lesson of our course, Building a CrewAI-Powered Travel Planner App with Flask. In this lesson, we will embark on an exciting journey to create a RESTful API using Flask, a popular web framework for Python. This API will serve as the backbone of our travel planner application, allowing users to submit travel planning requests and receive structured itinerary responses. Our API will integrate seamlessly with the CrewAI travel planner crew, which you have previously learned to work with. By the end of this lesson, you will have a solid understanding of how to set up and run a Flask application that interacts with CrewAI to deliver personalized travel plans.

## Setting Up Flask
Flask is a lightweight and flexible web framework that is perfect for building small to medium-sized web applications. It provides the tools needed to create web servers and handle HTTP requests. To get started with Flask on your local device, you would typically install it using `pip` with the command:

```Bash
pip install Flask
```


### Structuring the Project
Our project will be organized in a structured manner to support the design and functionality of our API. Here's how we'll organize our files:

```Plain text
app/
├── main.py                        # Main application file
└── travel_planner/
    ├── travel_planner_crew.py     # Main travel planner logic
    ├── models/
    │   ├── daily_plan.py          # Daily planning model
    │   ├── travel_itinerary.py    # Itinerary model
    │   └── attraction.py          # Attraction model
    ├── tools/
    │   └── custom_search_tool.py  # Custom search tool
    └── config/
        ├── tasks.yaml             # Task configurations
        └── agents.yaml            # Agent configurations
```

The `main.py` file will house the core logic of our Flask application, including initializing the app, defining routes, and handling requests. The `travel_planner` directory contains all the CrewAI-related components:

- `travel_planner_crew.py` implements the main travel planning logic
- The `models` directory contains Pydantic models for structuring our data
- The `tools` directory includes tools like our custom search tool
- The `config` directory stores YAML configuration files for tasks and agents

This modular structure ensures our code is organized, maintainable, and scalable as we build more complex features throughout the course.

### Initializing the Flask Application
To create our Flask application, we need to import the necessary modules and initialize the Flask app. Here's how we do it:

```Python

from flask import Flask, request, jsonify
from travel_planner.travel_planner_crew import TravelPlannerCrew

# Initialize Flask application
app = Flask(__name__)
```
In this code snippet:

- We import the Flask class along with the `request` and `jsonify` functions from the Flask package
    - The `request` object allows us to access incoming request data
    - The `jsonify` function helps us convert Python dictionaries to JSON responses
- We import our `TravelPlannerCrew` class from the travel_planner module
- The line `app = Flask(__name__)` creates a new Flask application instance

The `__name__` parameter is a Python special variable that gets set to the name of the module in which it is used. This helps Flask determine the root path of the application, which is essential for locating resources like templates and static files.

## Creating the Travel Planning Endpoint
The heart of our API is the `/api/plan` endpoint, which will handle travel planning requests. This endpoint will be designed to accept `POST` requests, allowing users to submit data such as the city they wish to visit, the number of days they plan to stay, and the number of attractions they want to see each day. Here is a snippet of the code that sets up this endpoint:

```Python
@app.route('/api/plan', methods=['POST'])
def plan_trip():
    # This function handles POST requests to the /api/plan endpoint
```

This code snippet shows how we define a route in Flask using the `@app.route` decorator. The `plan_trip` function will process the incoming request and return an appropriate response. When a user submits a travel planning request to this endpoint, Flask will automatically route the request to this function, which will then extract the necessary information, process it, and return a customized travel itinerary.

## Processing Form Data and Error Handling
For our travel planner API, we'll use form data to receive user inputs. Form data is a common way to submit information from web forms to servers. Flask makes it easy to access this data through the `request.form` object. Here's how we extract and process the form data, along with proper error handling:

```Python
@app.route('/api/plan', methods=['POST'])
def plan_trip():
    try:
        # Get form data
        city = request.form.get('city')
        days = int(request.form.get('days'))
        attractions_per_day = int(request.form.get('attractions_per_day'))

        # Calculate total attractions needed
        total_attractions = days * attractions_per_day

        # Further processing will be done here...
        
    except Exception as e:
        # Return an error message if there is an exception in the request processing
        return jsonify({"error": str(e)}), 400
```

In this code:

- We use `request.form.get()` to retrieve values from the submitted form
- We convert numeric values from strings to integers using `int()`
- We perform a simple calculation to determine the total number of attractions needed for the trip
- We wrap everything in a try-except block to catch any errors that might occur during processing
- If an error occurs (e.g., missing form fields or invalid data types), we return a JSON response with a 400 status code (Bad Request) and an error message

This robust approach ensures our API can gracefully handle invalid inputs while providing clear feedback to users about what went wrong.


## Integrating with the CrewAI Travel Planner

To generate a travel plan, we will integrate our API with the `CrewAI` travel planner. This involves using the `TravelPlannerCrew` class to initiate the travel planning process. We will prepare the necessary input parameters and invoke the travel crew to generate a personalized itinerary. Here is how this integration looks in code:

```Python
@app.route('/api/plan', methods=['POST'])
def plan_trip():
    try:
        # Get form data and calculate total attractions needed...

        try:
            # Initialize the TravelPlannerCrew instance
            travel_planner = TravelPlannerCrew()
            
            # Run the crew
            result = travel_planner.travel_crew().kickoff(inputs={
                "city": city,
                "days": days,
                "attractions_per_day": attractions_per_day,
                "total_attractions": total_attractions
            })
        except Exception as e:
            # Return an error message if there is an exception during crew execution
            return jsonify({"error": f"Error generating travel plan: {str(e)}"}), 500

        # Further processing will be done here...

    except Exception as e:
        return jsonify({"error": str(e)}), 400
```

This code demonstrates how we create an instance of `TravelPlannerCrew` and use it to kick off the travel planning process with the provided inputs. Notice the nested try-except block that specifically catches errors during the crew execution process. If something goes wrong while the CrewAI agents are working (such as API rate limits, connection issues, or agent failures), we return a 500 status code (Internal Server Error) with a descriptive error message. This separation of error handling allows us to distinguish between client-side errors (400 Bad Request) and server-side errors (500 Internal Server Error), providing more precise feedback to the client.

### Returning the Travel Itinerary as JSON
Once our CrewAI travel planner has generated an itinerary, we need to return it to the client in a structured JSON format. The Pydantic models we've defined help ensure our data is properly formatted and validated before being sent back to the user.

```Python
@app.route('/api/plan', methods=['POST'])
def plan_trip():
    try:
        # Get form data and calculate total attractions needed...
        
        # Create the crew and run it...

        # Check if the result has a pydantic model
        if result.pydantic:
            # Return the pydantic output in JSON format
            return jsonify(result.pydantic.model_dump())
        
        # Return an error message if no itinerary is generated
        return jsonify({"error": "No travel itinerary generated"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 400
```
The `jsonify` function from Flask automatically converts our Python dictionary (created by `model_dump()`) into a proper JSON response with the appropriate Content-Type headers, ensuring that clients can easily parse and use the data we return. If the result is not a Pydantic model, we return an error message indicating that no travel itinerary was generated, along with a 404 status code, to inform the client that the requested resource could not be found or created due to the absence of a valid itinerary.

## Running the Flask API
To see our API in action, we need to run the Flask server. This is done by executing the `app.run()` function, which starts the server on a specified host and port. In our case, we will run the server on all network interfaces, `port 3000`, with debug mode enabled for easier troubleshooting. Here is how you can start the server:

```Python
if __name__ == '__main__':
    # Only run the app when this file is executed directly
    app.run(
        host='0.0.0.0',  # Listen on all network interfaces
        port=3000,       # Run on port 3000
        debug=True       # Enable debug mode for development
    )
```
Once the server is running, you can test the API by sending a `POST` request to the `/api/plan` endpoint with the required data.

## Accessing the Plan Endpoint

A typical request might look like this:

```Plain text
POST http://localhost:3000/api/plan
Content-Type: application/x-www-form-urlencoded

city=New York&days=2&attractions_per_day=3
```

This POST request is sending form data to our API endpoint with three parameters:

- `city`: The destination city (New York)
- `days`: The number of days for the trip (2)
- `attractions_per_day`: The number of attractions to visit each day (3)

The Content-Type header indicates we're sending form-encoded data, which is how HTML forms typically submit information to servers. The POST method is used because we're creating a new resource (a travel plan) rather than just retrieving data.

And a successful response might look like this:

```JSON
{
  "city": "New York",
  "daily_plans": [
    {
      "attractions": [
        {
          "address": "Liberty Island, New York, NY 10004",
          "category": "Historical",
          "description": "An iconic symbol of freedom and democracy, the Statue of Liberty is located on Liberty Island.",
          "estimated_duration": "3 hours",
          "name": "Statue of Liberty"
        },
        ...
      ],
      "day_number": 1,
      "meal_suggestions": [
        "Lunch at a local deli near Battery Park (try bagels or a pastrami sandwich)",
        ...
      ]
    },
    ...
  ],
  "days": 2,
  "overall_tips": "Consider using the subway for quick transportation between attractions"
}
```


# Rendering a Basic HTML Page with Flask

In this lesson, we will focus on creating a basic HTML interface for our travel planner application. This interface will allow users to input their travel preferences and view the generated itinerary. By the end of this lesson, you will have a foundational understanding of how to render HTML pages using Flask, which is a crucial step in transitioning from backend API functionality to a user-facing application. This lesson builds on the RESTful API we developed in the previous lesson, and it sets the stage for creating a more interactive and engaging user experience.

Reviewing the Project Structure
Our project is organized to support both backend and frontend development. Here's a visual representation of the structure:

```Plain text
app/
├── main.py
├── travel_planner/
│   ├── travel_planner_crew.py
│   ├── models/
│   ├── tools/
│   └── config/
└── templates/
    └── index.html
```
The `templates` folder is a key component of this structure, as it stores all the HTML files that our Flask application will render. Within this folder, you will find the `index.html` file, which serves as the main interface for our travel planner application. This file will be the focus of our customization efforts as we build a user-friendly interface.

## Defining the Home Page Endpoint
To serve our HTML page, we need to define a route in our Flask application that renders the `index.html` file. This is done by setting up a home page endpoint using the `@app.route` decorator. Flask provides a powerful function called `render_template` that allows us to serve HTML files to users. This function is essential for rendering HTML pages and dynamically inserting data into templates. When a user accesses a specific route in our Flask application, `render_template` locates the corresponding HTML file in the `templates` folder and serves it to the user. This process enables us to create dynamic web pages that can display data from our backend API.

```Python
from flask import Flask, render_template, request, jsonify
from travel_planner.travel_planner_crew import TravelPlannerCrew

# Initialize Flask application
app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    # Render the HTML template
    return render_template('index.html')
    
# Travel planning route and configurations to start the server...
```

In this code snippet, the `index` function is associated with the root URL (`'/'`). When a user accesses this URL, Flask will call the `index` function, which in turn uses `render_template` to serve the `index.html` file. This integration allows us to seamlessly connect our backend logic with the frontend interface.

## Creating and Customizing the HTML Template
Let's take a look at the basic structure of our `index.html` file. This file includes essential elements such as the `<head>`, `<body>`, a form for user input, and a section for displaying results. The `<head>` contains metadata and the title of the page, while the `<body>` houses the main content. The form allows users to input their travel preferences, and the results section will display the generated itinerary.

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Travel Planner</title>
</head>
<body>
    <h1>Travel Planner</h1>
    
    <div>
        <h5>Plan Your Trip</h5>
        <!-- Form for trip planning -->
        <form id="tripForm">
            <div>
                <label for="city">City</label>
                <input type="text" id="city" name="city" required>
            </div>
            <div>
                <label for="days">Number of Days</label>
                <input type="number" id="days" name="days" min="1" required>
            </div>
            <div>
                <label for="attractions_per_day">Number of Attractions per Day</label>
                <input type="number" id="attractions_per_day" name="attractions_per_day" min="1" required>
            </div>
            <button type="submit">Plan Trip</button>
        </form>
    </div>

    <!-- Results Section -->
    <div id="resultsCard" style="display: none;">
        <h5>Your Travel Itinerary</h5>
        <div id="resultsContent"></div>
    </div>
</body>
</html>
```

The HTML template includes a form designed to capture user input for travel planning, with fields for the city, number of days, and attractions per day, each accompanied by labels and validation to ensure accurate data entry. Upon submission, this form will eventually trigger backend processes to generate a travel itinerary. The results section, initially hidden, is designated to display the itinerary once available. This basic structure will be improved in future lessons to enhance functionality and user interaction.



# Adding Simulated Functionality with JavaScript

In the previous sections, we laid the groundwork for our travel planner application by creating a RESTful API with **Flask** and rendering a basic HTML page. Now, we are ready to enhance the user experience by adding client-side **JavaScript**. This lesson will focus on implementing JavaScript to handle form submissions, simulate API calls, and dynamically render content. By the end of this lesson, you will be able to create a more interactive and engaging application that responds to user input in real-time.



## Reviewing the Project Structure
Before we dive into linking JavaScript to our HTML, let's focus on the specific file we are creating and its location within the project structure.

```Plain text
app/
├── main.py
├── travel_planner/
├── static/
│   └── js/
│       └── travel-planner.js  # JavaScript file for enhancing interactivity
└── templates/
    └── index.html
```

We are creating the `travel-planner.js` file inside the `static/js/` directory. This file will contain the JavaScript code responsible for enhancing the interactivity of our travel planner application. By placing it in the `static/js/` directory, we ensure that it is served correctly by Flask as a static asset, allowing us to link it to our `index.html` file for client-side functionality.

## Linking JavaScript to HTML
Now that we have created the `travel-planner.js` file in the `static/js/` directory, it's time to link this JavaScript file to our HTML page. This is done by including a `<script>` tag in the `index.html` file. In Flask, we use the `url_for` function to correctly reference the static JavaScript file. This ensures that our JavaScript code is loaded and ready to enhance the page's functionality.

Here's how your `index.html` file should look, with comments indicating where the rest of the code should be:

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Travel Planner</title>
</head>
<body>
    <!-- Form for trip planning... -->

    <!-- Results Section... -->

    <!-- Link to the JavaScript file for handling form submission and rendering results -->
    <script src="{{ url_for('static', filename='js/travel-planner.js') }}"></script>
</body>
</html>
```
This line of code is placed just before the closing `</body>` tag in your HTML file, ensuring that the JavaScript is loaded after the HTML content. By linking the JavaScript file, we enable the dynamic features and interactivity that will enhance the user experience of our travel planner application.

## Preventing Default Form Submission and Initializing UI Elements
With our JavaScript file linked to the HTML, we are ready to start writing the JavaScript code in the `travel-planner.js` file. Our first task is to set up the form to handle submissions in a way that allows us to process the data and update the UI dynamically without refreshing the page.

Step-by-Step Guide:

1. **Add an Event Listener to the Form**: We begin by adding an event listener to the form. This listener will trigger an `async` function whenever the form is submitted. Using `async` allows us to use the `await` keyword inside the function, which is useful for handling asynchronous operations like simulating API calls.

1. **Prevent Default Form Submission**: By default, submitting a form causes the page to reload. We want to prevent this behavior so that we can handle the form data with JavaScript. We do this by calling `e.preventDefault()`.

1. **Show Loading Spinner and Results Card**: To provide feedback to the user that their submission is being processed, we display a loading spinner. We also prepare the results card where the itinerary will be displayed by clearing any previous content.

Here's how you can implement these steps in your `travel-planner.js` file:

```JavaScript
// Add an event listener to the form to handle submissions
document.getElementById('tripForm').addEventListener('submit', async function(e) {
    // Prevent the default form submission behavior
    e.preventDefault();

    // Show loading spinner and results card
    document.getElementById('loadingSpinner').style.display = 'block';
    document.getElementById('resultsCard').style.display = 'block';
    document.getElementById('resultsContent').innerHTML = '';

    // Further processing of the form data will be done here...
});
```
In this code, we set up an event listener on the form with the ID `tripForm` to handle submissions. By calling `e.preventDefault()`, we stop the default form submission, which would normally reload the page. Instead, we display a loading spinner and prepare the results card by clearing any previous content. This approach allows us to process the form data and update the user interface dynamically, providing a seamless and interactive experience for the user.

## Handling Form Data with FormData Object
After intercepting the form submission, we can access the form data using the `FormData` object. This object provides a convenient way to extract user input values from the form fields. We can then process these values, such as converting them to the appropriate data types for further use in our application logic.

```JavaScript
document.getElementById('tripForm').addEventListener('submit', async function(e) {
    // Code to prevent default and initialize UI...

    // Create a FormData object to easily access form input values
    const formData = new FormData(this);

    // Extract the city name from the form data
    const city = formData.get('city');

    // Extract and convert the number of days to an integer
    const days = parseInt(formData.get('days'));

    // Extract and convert the number of attractions per day to an integer
    const attractionsPerDay = parseInt(formData.get('attractions_per_day'));

    // Further processing of the form data will be done here...
});
```
Using the `FormData` object simplifies the process of gathering and manipulating form data, allowing us to focus on the core functionality of our application.

## Simulating API Calls with Error Handling and UI Feedback
In this context, simulating API calls allows us to develop and test the client-side logic and user interface before a real backend or external service is available. This approach helps ensure that our application's interactive features work as intended, even while the backend is still under development.

To create a realistic user experience, we simulate an API call using a `try-catch-finally` block. The `try` block contains a simulated delay using `setTimeout`, which mimics the time taken for an API response. We use the `await` keyword to pause the execution of the function until the simulated delay is complete, just as we would when waiting for a real API call to return data. If an error occurs during this process, the `catch` block displays an error message to the user. The `finally` block ensures that the loading spinner is hidden, providing a seamless user experience regardless of the outcome.

```JavaScript
document.getElementById('tripForm').addEventListener('submit', async function(e) {
    // Code to prevent default, initialize UI, and handle form data...

    try {
        // Simulate a delay of 2 seconds to mimic an API call
        await new Promise(resolve => setTimeout(resolve, 2000));

        // Simulate and process API response data...

    } catch (error) {
        document.getElementById('resultsContent').innerHTML = `
            <div>
                An error occurred while planning your trip. Please try again.
            </div>
        `;
    } finally {
        // Hide loading spinner
        document.getElementById('loadingSpinner').style.display = 'none';
    }
});
```
By implementing this structure, we provide users with feedback during the processing phase and handle any potential errors gracefully, ensuring a robust and user-friendly application.

## Simulating Response Data
To effectively test our application's functionality, we simulate response data that mimics what a real API might return. This involves creating mock data for the travel itinerary based on user input, such as the city, number of days, and attractions per day. By generating this data, we can ensure that our application processes and displays information correctly without relying on a live API.

```JavaScript
try {
    // Simulate a delay of 2 seconds to mimic an API call
    await new Promise(resolve => setTimeout(resolve, 2000));

    // Simulate API response data
    const data = {
        city: city,
        days: days,
        daily_plans: []
    };
    
    // Create simple daily plans
    for (let i = 1; i <= days; i++) {
        // Initialize an empty array to store the attractions for this day
        const attractions = [];
        // Generate the specified number of attractions for this day
        for (let j = 1; j <= attractionsPerDay; j++) {
            attractions.push({
                name: `${city} Attraction ${j}`,
                category: "Tourist Spot",
                estimated_duration: "2 hours",
                address: `Some Street`,
                description: `Description for attraction ${j} in ${city}.`
            });
        }
        // Create a daily plan object for each day
        data.daily_plans.push({
            day_number: i,
            attractions: attractions,
            meal_suggestions: [
                `Breakfast at ${city} Café`,
                `Lunch at ${city} Bistro`,
                `Dinner at ${city} Restaurant`
            ]
        });
    }
    
    // Add overall travel tips 
    data.overall_tips = `Travel tips for ${city}: Bring comfortable shoes and a map.`;

    // Displaying the simulated data will be done here...
}
```

In the code provided, we simulate response data to test how our application processes and displays it. This approach allows us to ensure that the user interface behaves as expected without relying on a live API. Here's a detailed explanation of what we did in the code:

1. **Create Simulated API Response Data**: We construct an object named `data` that mimics the structure of a real API response. This object includes details such as the city, number of days, and daily plans.

1. **Generate Daily Plans**: We loop through the number of days specified by the user and create a simple itinerary for each day. For each day, we generate a list of attractions based on the number of attractions per day specified by the user. Each attraction includes a name, category, estimated duration, and description.

1. **Add Overall Tips**: We include a section for overall travel tips, providing general advice for the trip.

By simulating this data, we can proceed to test how the application processes and displays it. This ensures that the user interface behaves as expected, allowing us to verify that the dynamic rendering of the itinerary works correctly.

## Setting Up the Itinerary Display
With the simulated response data in hand, the next step is to dynamically render the itinerary on the page. We start by initializing an HTML string that will hold the itinerary content and checking if the daily plans data exists and is in the expected format.

```JavaScript
document.getElementById('tripForm').addEventListener('submit', async function(e) {
    // Code to prevent default, initialize UI, handle form data, simulate delay...

    try {
        // Simulate a delay and generate response data...

        // Initialize the HTML string for the itinerary container
        let html = '<div class="itinerary">';
        
        // Check if daily plans exist and are in an array format
        if (data.daily_plans && Array.isArray(data.daily_plans)) {
            // Further processing of daily plans will be done here...
        } else {
            // Display a message if no itinerary data is available
            html += '<div>No itinerary data available</div>';
        }

        // Code to inject the HTML content into the results section...
    } catch (error) {
        // Error handling...
    } finally {
        // Hide loading spinner...
    }
});
```
In this code, we begin by creating a variable `html` that will store the HTML content for our itinerary. We initialize it with a div element that has a class of "itinerary" to serve as a container. We then check if the `data.daily_plans property` exists and is an array. This validation ensures that we have valid data to work with before attempting to render the itinerary. If the data is not available or not in the expected format, we display a message to the user indicating that no itinerary data is available.

## Iterating Through Each Day's Plan
Once we've confirmed that the daily plans data exists, we need to iterate through each day's plan to construct the HTML content. This involves creating a structure that will display the day number, attractions, and meal suggestions for each day.

```JavaScript
if (data.daily_plans && Array.isArray(data.daily_plans)) {
    // Iterate over each day's plan to construct the itinerary details
    data.daily_plans.forEach((day) => {
        // Code to construct HTML for each day...
    });
    
    // Code to add overall tips...
} else {
    html += '<div>No itinerary data available</div>';
}
```
Here, we set up the structure for iterating over each day's plan in the `data.daily_plans array`. We use the `forEach` method to loop through each day, which allows us to access the details for that specific day. Inside this loop, we will construct the HTML content for each day's itinerary, including attractions and meal suggestions. After processing all days, we'll add overall tips to provide general advice for the trip. If the daily plans data is not available, we display a message to inform the user.

## Building Detailed Daily Activities
For each day in the itinerary, we construct detailed HTML content that includes the day number, a list of attractions with their details, and meal suggestions. This creates a comprehensive view of the daily activities for the user.

```JavaScript
if (data.daily_plans && Array.isArray(data.daily_plans)) {
    data.daily_plans.forEach((day) => {
        html += `
            <div class="day-plan">
                <h6>Day ${day.day_number}</h6>
                <ul>
                    ${day.attractions.map(attraction => `
                        <li>
                            <strong>${attraction.name}</strong><br>
                            ${attraction.category} • <small>${attraction.estimated_duration}</small><br>
                            ${attraction.address ? `<small>${attraction.address}</small><br>` : ''}
                            ${attraction.description}
                        </li>
                    `).join('')}
                </ul>

                ${day.meal_suggestions ? `
                    <div>
                        <p>Meal Suggestions:</p>
                        <ul>
                            ${day.meal_suggestions.map(suggestion => `
                                <li>${suggestion}</li>
                            `).join('')}
                        </ul>
                    </div>
                ` : ''}
            </div>
        `;
    });
}
```
In this implementation, we use template literals to construct the HTML content for each day's plan. For each day, we create a div with a class of "day-plan" and include an h6 heading that displays the day number. We then create an unordered list to display the attractions for that day. Using the `map` method, we iterate over each attraction and create a list item that includes the attraction's name, category, estimated duration, and description. The `join('')` method combines all the list items into a single string.

We also check if meal suggestions are available for the day using a `conditional (ternary) operator`. If meal suggestions exist, we create another section that lists them. This approach ensures that we only display the meal suggestions section if there are actual suggestions to show. The resulting HTML provides a detailed and organized view of each day's activities.

## Adding Travel Tips and Finalizing the Display
After displaying the daily plans, we add a section for overall travel tips if they are available. These tips provide general advice for the trip. Finally, we inject the constructed HTML content into the results section of the page, making the itinerary visible to the user.

```JavaScript
if (data.daily_plans && Array.isArray(data.daily_plans)) {
    // Code to iterate over each day's plan...
    
    // Add overall tips if available
    if (data.overall_tips) {
        html += `
            <div>
                <h6>Overall Tips</h6>
                <div>
                    ${data.overall_tips}
                </div>
            </div>
        `;
    }
} else {
    html += '<div>No itinerary data available</div>';
}

// Inject the HTML content into the results section
document.getElementById('resultsContent').innerHTML = html;
```
In this final section, we check if overall tips are available by verifying that the `data.overall_tips` property exists. If it does, we append a new div to our HTML string that contains an h6 heading labeled "Overall Tips" and a div that displays the tips content. This provides users with general advice for their trip, such as what to pack or local customs to be aware of.

After constructing all the HTML content for the itinerary, we use the `innerHTML` property to inject this content into the element with the ID `"resultsContent"`. This replaces any previous content in that element with our newly generated itinerary. By doing this, we dynamically update the page to display the travel plan without requiring a page refresh, providing a seamless and interactive user experience.