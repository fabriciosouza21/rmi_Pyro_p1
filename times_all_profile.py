from run_analise import run_analise
import Pyro4

conection = Pyro4.Proxy("PYRONAME:example.interface")


def time_search_users_course():
    operation = conection.all_profile
    operation_name = "all_profile"
    result = run_analise(operation=operation,
                         operation_name=operation_name)
    return result


print(time_search_users_course())
