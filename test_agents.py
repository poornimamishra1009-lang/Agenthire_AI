from mcp.agent_coordinator import AgentCoordinator

coordinator = AgentCoordinator()

result = coordinator.run_agents(
    experience="1 year",
    skills="Python, FastAPI, MLflow",
    salary="12",
    location="Remote"
)

print(result)