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



# Creating a Simple Agent

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


