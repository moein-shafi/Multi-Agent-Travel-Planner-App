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



## Creating a Simple Agent

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