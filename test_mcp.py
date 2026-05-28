from mcp.agent_coordinator import AgentCoordinator

coordinator = AgentCoordinator()

coordinator.update(
    "skills",
    "Python, FastAPI, MLflow"
)

coordinator.update(
    "experience",
    "1 year"
)

print(
    coordinator.get_full_context()
)