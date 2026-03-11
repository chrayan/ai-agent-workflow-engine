from fastapi import FastAPI
from agent.planner import Planner
from agent.executor import Executor

app = FastAPI()

planner = Planner()
executor = Executor()


@app.get("/task")

def run(task: str):

    tool = planner.plan(task)

    result = executor.execute(tool, task)

    return {"tool": tool, "result": result}
