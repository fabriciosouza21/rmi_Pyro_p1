from communication_time import communication_time
from descriptive_math import descriptive_math
import Pyro4


def main():
    conection = Pyro4.Proxy("PYRONAME:example.interface")
    operation = conection.search_users_course
    operation_name = "search_users_course"
    course = "ciencia da computacao"
    times = communication_time(
        operation_name=operation_name, operation=operation, number_executions=10000)
    data_times = times.run(parameter1=course)
    analise_times = descriptive_math(data_times)
    run_analise_times = analise_times.analysis()
    print(run_analise_times)


if __name__ == '__main__':
    main()
