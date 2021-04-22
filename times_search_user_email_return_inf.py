from run_analise import run_analise
import Pyro4

conection = Pyro4.Proxy("PYRONAME:example.interface")


def times_search_user_email_return_inf():
    operation = conection.search_user_email_return_inf
    operation_name = "search_user_email_return_inf"
    search = "fffff@gmail.com"
    result, _ = run_analise(operation=operation,
                            operation_name=operation_name, parameter1=search)
    return result


print(times_search_user_email_return_inf())
