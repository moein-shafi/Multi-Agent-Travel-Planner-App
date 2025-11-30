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

    