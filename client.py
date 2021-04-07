import Pyro4

conection = Pyro4.Proxy("PYRO:interface@localhost:52119")

def show_users(users):
    for user in users:
        print('\nUsuário: {} {}'.format(user['nome'], user['sobrenome']))
        print('Email: ', user['email'])
        print('Residência: ', user['residencia'])
        print('Formação acadêmica: ', user['formacao academica'])
        print('Habilidades: ', user['habilidade'])
        print('Experiência: ', user['experiencia'])

def filtrar_dados():
    while True: 
        print('====================================================')
        print('[1] Listar todos os dados dos perfis filtrados')
        print('[2] Listar 1 dado dos perfis filtrados')
        print('[3] Voltar')
        opcao_filtro = int(input('Informe uma opção: '))
        print('====================================================')
        
        if(opcao_filtro == 1):
            field = input("Qual o campo que deseja pesquisar? ").strip()
            search = input("Informe {}: ".format(field)).strip()

            users = conection.data(field, search)

            show_users(users)

            break
        elif(opcao_filtro == 2):
            field = input("Qual o campo que deseja pesquisar? ").strip()
            search = input("Informe {}: ".format(field)).strip()
            dado = input("Informe qual dado do perfil deve aparecer: ".strip())

            users = conection.data(field, search)

            for user in users:
                print('\n{}: {}'.format(field, user[field]))
                print('{}: {}'.format(dado, user[dado]))
            
            break
        elif(opcao_filtro == 3):
            break
        else:
            print('Opção inválida!')

def main():
    while True:
        print('====================================================')
        print('[1] Adicionar perfil')
        print('[2] Editar perfil')
        print('[3] Listar todos os perfis')
        print('[4] Filtrar perfis')
        print('[5] Sair')
        opcao = int(input('Informe uma opção: '))
        print('====================================================')
        
        if(opcao == 1):
            break #Adicionar perfil
        elif(opcao == 2):
            break #Editar perfil
        elif(opcao == 3):
            users = conection.data(None, None)

            show_users(users)
        elif(opcao == 4):
            filtrar_dados()
        elif(opcao == 5):
            print('\nEncerrando...')
            break
        else:
            print('\nOpção inválida!')

if __name__ == '__main__':
    main()