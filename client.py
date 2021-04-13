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
        print('[2] Listar dados específicos dos perfis filtrados')
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
            dado = []
            field = input("Qual o campo que deseja pesquisar? ").strip()
            search = input("Informe {}: ".format(field)).strip()
            dado.append(input("Informe qual dado do perfil deve aparecer: ".strip()))
            
            while True:
                op_dado = int(input("\nDeseja adicionar mais um dado? [1-Sim/2-Não] "))
                if op_dado == 1:
                    dado.append(input("Informe qual dado do perfil deve aparecer: ".strip()))
                elif op_dado == 2:
                    break
                else:
                    print('Opção inválida!')

            users = conection.data(field, search)

            for user in users:
                print('\n{}: {}'.format(field, user[field]))
                for i in range(0, len(dado)):
                    print('{}: {}'.format(dado[i], user[dado[i]]))

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
            adicionar_perfil()
        elif(opcao == 2):
            break  # Editar perfil
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


def adicionar_perfil():
    perfil = {}
    habilidades = []
    experiencias = []
    formacao_academica = []

    print("adicinando perfil")
    perfil["nome"] = input("Nome: ")
    perfil["sobrenome"] = input("Sobrenome: ")
    perfil["email"] = input("email: ")
    perfil["residencia"] = input("residencia: ")

    formacao = input("formacao academica: ")
    formacao_academica.append(formacao)
    perfil["formacao academica"] = formacao_academica

    habilidade = input("Habilidade: ")
    habilidades.append(habilidade)
    perfil["habilidades"] = habilidades

    experiencia = input("Experiencia: ")
    experiencias.append(experiencia)
    perfil["experiencia"] = experiencias

    conection.adicionar_perfil(perfil)
    # print(conection.profiles.find_all())


if __name__ == '__main__':
    main()
