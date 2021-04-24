from src.run_analise import run_analise
import Pyro4

conection = Pyro4.Proxy("PYRONAME:example.interface")


def time_search_user_email_return_xp():
    operation = conection.search_user_email_return_xp
    operation_name = "search_user_email_return_xp"
    search = "fffff@gmail.com"
    result, _ = run_analise(operation=operation,
                            operation_name=operation_name, parameter1=search)
    return result


print(time_search_user_email_return_xp())
