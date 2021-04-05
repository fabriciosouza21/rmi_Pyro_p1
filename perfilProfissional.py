import json
from repositorio import RepositorioProfessionalProfile
profissionalProfile = RepositorioProfessionalProfile()
usuarios = profissionalProfile.find("residencia", "belem")
print(usuarios)
