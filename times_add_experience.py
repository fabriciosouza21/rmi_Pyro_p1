from run_analise import run_analise
import Pyro4

conection = Pyro4.Proxy("PYRONAME:example.interface")


def times_add_experience():
    operation = conection.add_experience
    operation_name = "add_experience"
    paramenter1 = "fffff@gmail.com"
    paramenter2 = "programação em python web"
    result = run_analise(operation=operation,
                         operation_name=operation_name,
                         parameter1=paramenter1,
                         parameter2=paramenter2)
    return result


print(times_add_experience())
