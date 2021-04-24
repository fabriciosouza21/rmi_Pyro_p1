import timeit


class communication_time:
    def __init__(self, operation_name, operation,
                 number_executions=200):
        self.number_executions = number_executions
        self.operation_name = operation_name
        self.operation = operation

    def run(self, parameter1=None, parameter2=None):
        times_execution = []
        for i in range(self.number_executions):

            if parameter2:
                start = timeit.default_timer()
                self.operation(parameter1, parameter2)
                end = timeit.default_timer()
                time_execution = end - start
                times_execution.append(time_execution)
            elif parameter1:
                start = timeit.default_timer()
                self.operation(parameter1)
                end = timeit.default_timer()
                time_execution = end - start
                times_execution.append(time_execution)
            else:
                start = timeit.default_timer()
                self.operation()
                end = timeit.default_timer()
                time_execution = end - start
                times_execution.append(time_execution)

        return times_execution
