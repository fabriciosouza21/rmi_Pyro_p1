import Pyro4

conection = Pyro4.Proxy("PYRO:interface@localhost:52119")

def filtrar_dados():
    while True: 
        print('====================================================')
        print('[1] Listar todos os dados dos perfis filtrados')
        print('[2] Listar 1 dado dos perfis filtrados')
        print('[3] Sair')
        opcao_filtro = int(input('Informe uma opção: '))
        print('====================================================')
        
        if(opcao_filtro == 1):
            break
        elif(opcao_filtro == 2):
            field = input("Qual o campo que deseja pesquisar? ").strip()
            search = input("Informe {}: ".format(field)).strip()

            users = conection.data(field, search)

            for user in users:
                print('\nUsuário: {} {}'.format(user['nome'], user['sobrenome']))
                print('Email: ', user['email'])
                print('Residência: ', user['residencia'])
                print('Formação acadêmica: ', user['formacao academica'])
                print('Habilidades: ', user['habilidade'])
                print('Experiência: ', user['experiencia'])
            break
        elif(opcao_filtro == 3):
            break
        else:
            print('Opção inválida!')

def main():
    while True:
        print('====================================================')
        print('[1] Listar todos os perfis')
        print('[2] Filtrar perfis')
        print('[3] Sair')
        opcao = int(input('Informe uma opção: '))
        print('====================================================')
        
        if(opcao == 1):
            pass
        elif(opcao == 2):
            filtrar_dados()
        elif(opcao == 3):
            print('\nEncerrando...')
            break
        else:
            print('\nOpção inválida!')

if __name__ == '__main__':
    main()