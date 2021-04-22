from run_analise import run_analise
import Pyro4

conection = Pyro4.Proxy("PYRONAME:example.interface")


def time_search_users_course():
    operation = conection.search_users_course
    operation_name = "search_users_course"
    course = "ciencia da computacao"
    result, _ = run_analise(operation=operation,
                            operation_name=operation_name, parameter1=course)
    return result


print(time_search_users_course())
