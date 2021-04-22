from run_analise import run_analise
import Pyro4

conection = Pyro4.Proxy("PYRONAME:example.interface")


def times_search_residence():
    operation = conection.search_residence
    operation_name = "search_residence"
    paramenter = "belem"
    result, _ = run_analise(operation=operation,
                            operation_name=operation_name, parameter1=paramenter)
    return result


print(times_search_residence())
