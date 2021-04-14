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

def search_users_course():
    course = input("Digite o Curso!! \n")
    print('retorno usuario do mesmo curso',conection.search_users_course(course))

def search_user_email_return_xp():
    email = input("digite o email da busca \n")
    print('retorno do usuario busca pelo email em busca da experiencia:',conection.search_user_email_return_xp(email))
def search_user_email_return_inf():
    email = input("digite o email da busca \n")
    print('informações retornadas baseadas no email',conection.search_user_email_return_inf(email))

def main():
    while True:
        print('====================================================')
        print('[1] Adicionar perfil')
        print('[2] Editar perfil')
        print('[3] Listar todos os perfis')
        print('[4] Filtrar perfis')
        print('[5] retorna lista de curso especifico')
        print('[7] dado o email do perfil, retornar sua experiência')
        print('[9] dado o email de um perfil, retornar suas informações')

        print('[6] Habilidades por cidade')

        print('[0] Sair')
        opcao = int(input('Informe uma opção: '))
        print('====================================================')

        if(opcao == 1):
            adicionar_perfil()
        elif(opcao == 2):
            break  # Editar perfil
        elif(opcao == 3):
            users = conection.all_profile()

            show_users(users)
        elif(opcao == 4):
            filtrar_dados()

        elif(opcao == 5):
            search_users_course()
        elif(opcao == 7):
            search_user_email_return_xp()
        elif(opcao == 9):
            search_user_email_return_inf()
        elif(opcao == 6):
            ability_residence()
        elif (opcao == 8):
            add_experience()
        elif(opcao == 0):
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


def ability_residence():
    residence = input("residencia na qual deseja localiza as habilidades: ")
    profiles = conection.search_residence(residence)

    habilidades = []
    list_unique_habilidades = []

    for user in profiles:
        for habilidade in user["habilidade"]:
            habilidades.append(habilidade)

    unique_habilidades = set(habilidades)
    for habilidade in unique_habilidades:
        list_unique_habilidades.append(habilidade)

    print(f"habilidades presente em {residence}")
    for habilidade in list_unique_habilidades:
        print(habilidade)


def add_experience():
    email = input("email: ")
    experiencia = input("experiecia: ")
    status = conection.add_experience(email, experiencia)
    print(conection.all_profile())


if __name__ == '__main__':
    main()
