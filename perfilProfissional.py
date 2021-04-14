import json
from repositorio import RepositorioProfessionalProfile
perfil = {}
perfil = {
    "email": "fabricio@gmail.com",
    "nome": "fabricio",
    "sobrenome": "souza",
    "residencia": "belem",
    "formação academica": [
            "ciencia da computacao"
    ],
    "habilidade": [
        "programação web"
    ],
    "experiencia": [
        "projeto pessoais em django"
    ]
}
profissionalProfile = RepositorioProfessionalProfile()
search=profissionalProfile.find('email' ,'yannfabriciogmail.com')
print(search)
#profissionalProfile.save(perfil)
#usuarios = profissionalProfile.find_all()
#print(usuarios)
