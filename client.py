import Pyro4

conection = Pyro4.Proxy("PYRO:interface@localhost:52119")

field = input("Qual o campo que deseja pesquisar? ").strip()
search = input("Informe {}: ".format(field)).strip()

users = conection.data(field, search)

print('\nListando usuários\n')

for user in users:
  print('Usuário: {} {}'.format(user['nome'], user['sobrenome']))
  print('Email: ', user['email'])
  print('Residência: ', user['residencia'])
  print('Formação acadêmica: ', user['formacao academica'])
  print('Habilidades: ', user['habilidade'])
  print('Experiência: ', user['experiencia'])
  print('')