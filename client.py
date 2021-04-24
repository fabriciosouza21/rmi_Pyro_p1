import Pyro4

conection = Pyro4.Proxy("PYRONAME:example.interface")


def show_users(users):
    for user in users:
        print('\nUsuário: {} {}'.format(user['nome'], user['sobrenome']))
        print('Email: ', user['email'])
        print('Residência: ', user['residencia'])
        print('Formação acadêmica: ', user['formacao academica'])
        print('Habilidades: ', user['habilidade'])
        print('Experiência: ', user['experiencia'])


def filter_data():
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
            dado.append(
                input("Informe qual dado do perfil deve aparecer: ").strip())

            while True:
                op_dado = int(
                    input("\nDeseja adicionar mais um dado? [1-Sim/2-Não] "))
                if op_dado == 1:
                    dado.append(
                        input("Informe qual dado do perfil deve aparecer: ").strip())
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


def search_users_course():
    course = input("Digite o Curso: ")
    users_course = conection.search_users_course(course)
    print('Usuários que cursam {}: '.format(course))
    show_users(users_course)


def search_user_email_return_xp():
    email = input("Digite o email da busca: ")
    exp_user = conection.search_user_email_return_xp(email)
    print('Experiência de um usuário a partir do email {}: \n'.format(email))

    for i in range(len(exp_user[0])):
        print('Experiência {}: {}'.format(i+1, exp_user[0][i]))


def search_user_email_return_inf():
    email = input("Digite o email da busca: ")
    infos_user = conection.search_user_email_return_inf(email)
    print('Informações de um usuário a partir do email {}: '.format(email))
    show_users(infos_user)


def adicionar_perfil():
    perfil = {}
    habilidades = []
    experiencias = []
    formacao_academica = []

    print("Adicinando perfil\n")
    perfil["nome"] = input("Nome: ")
    perfil["sobrenome"] = input("Sobrenome: ")
    perfil["email"] = input("Email: ")
    perfil["residencia"] = input("Residência: ")

    formacao = input("Formação acadêmica: ")
    formacao_academica.append(formacao)
    perfil["formacao academica"] = formacao_academica

    habilidade = input("Habilidade: ")
    habilidades.append(habilidade)
    perfil["habilidade"] = habilidades

    experiencia = input("Experiência: ")
    experiencias.append(experiencia)
    perfil["experiencia"] = experiencias

    conection.adicionar_perfil(perfil)


def ability_residence():
    residence = input("Residência na qual deseja localizar as habilidades: ")
    profiles = conection.search_residence(residence)

    habilidades = []
    list_unique_habilidades = []

    for user in profiles:
        for habilidade in user["habilidade"]:
            habilidades.append(habilidade)

    unique_habilidades = set(habilidades)
    for habilidade in unique_habilidades:
        list_unique_habilidades.append(habilidade)

    print(f"Habilidades presente em {residence}: ")
    for habilidade in list_unique_habilidades:
        print(habilidade)


def add_experience():
    print("Adicionar experiência\n")
    email = input("Email: ")
    experiencia = input("Experiência: ")
    conection.add_experience(email, experiencia)


def main():
    while True:
        print('====================================================')
        print('[1] Adicionar perfil')
        print('[2] Listar todos os perfis')
        print('[3] Filtrar perfis')
        print('[4] Retornar lista de curso específico')
        print('[5] Habilidades por cidade')
        print('[6] Dado o email do perfil, retornar sua experiência')
        print('[7] Adicionar nova experiencia dado o email')
        print('[8] Dado o email de um perfil, retornar suas informações')
        print('[0] Sair')
        opcao = int(input('Informe uma opção: '))
        print('====================================================')

        if(opcao == 1):
            adicionar_perfil()

        elif(opcao == 2):
            users = conection.all_profile()
            show_users(users)

        elif(opcao == 3):
            filter_data()

        elif(opcao == 4):
            search_users_course()

        elif(opcao == 5):
            ability_residence()

        elif(opcao == 6):
            search_user_email_return_xp()

        elif (opcao == 7):
            add_experience()

        elif(opcao == 8):
            search_user_email_return_inf()

        elif(opcao == 0):
            print('\nEncerrando...')
            break
        else:
            print('\nOpção inválida!')


if __name__ == '__main__':
    main()
