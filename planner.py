class Planner:

    def plan(self, task):

        if "calculate" in task:
            return "calculator"

        if "search" in task:
            return "web_search"

        return "calculator"
