from tools.calculator import calculate
from tools.web_search import search

class Executor:

    def execute(self, tool, task):

        if tool == "calculator":
            return calculate(task)

        if tool == "web_search":
            return search(task)
