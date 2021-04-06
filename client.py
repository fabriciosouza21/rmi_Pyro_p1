import Pyro4

teste = Pyro4.Proxy('PYRO:interface@localhost:53546')
print(teste.test())