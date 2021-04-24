from src.run_analise import run_analise
import Pyro4

conection = Pyro4.Proxy("PYRONAME:example.interface")


def time_all_profile():
    operation = conection.all_profile
    operation_name = "all_profile"
    result, _ = run_analise(operation=operation,
                            operation_name=operation_name)
    return result


print(time_all_profile())
