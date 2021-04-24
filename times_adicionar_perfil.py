from src.run_analise import run_analise
import Pyro4

conection = Pyro4.Proxy("PYRONAME:example.interface")


def times_adicionar_perfil():
    operation = conection.adicionar_perfil
    operation_name = "adicionar_perfil"
    paramenter = {
        "email": "fabricio@gmail.com",
        "nome": "fabricio",
        "sobrenome": "souza",
        "residencia": "ananideua",
        "formacao academica": [
            "ciencia da computacao"
        ],
        "habilidade": [
            "programação em python"
        ],
        "experiencia": [
            "projeto pessoais em django"
        ]
    }
    result, _ = run_analise(operation=operation,
                            operation_name=operation_name,
                            parameter1=paramenter)
    return result


print(times_adicionar_perfil())
