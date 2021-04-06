import Pyro4

teste = Pyro4.Proxy("PYRO:interface@localhost:52119")

field = input("Qual o campo que deseja pesquisar? ").strip()
search = input("Informe {}: ".format(field)).strip()

print(teste.dados(field, search))