from communication_time import communication_time
from descriptive_math import descriptive_math


def run_analise(operation, operation_name, parameter1=None, parameter2=None):
    times = communication_time(
        operation_name=operation_name,
        operation=operation,
        number_executions=200
    )
    if parameter2:
        get_times = times.run(parameter1, parameter2)
    else:
        get_times = times.run(parameter1)
    analise = descriptive_math(get_times)
    analise_times = analise.analysis()
    return analise_times
