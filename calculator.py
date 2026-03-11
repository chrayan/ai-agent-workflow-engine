def calculate(task):

    expression = task.replace("calculate", "")

    try:
        result = eval(expression)
        return result
    except:
        return "error"
