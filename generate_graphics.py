import matplotlib.pyplot as plt
from run_analise import run_analise
from descriptive_math import descriptive_math
import Pyro4

conection = Pyro4.Proxy("PYRONAME:example.interface")
class Pizza_graphic:
    def __init__(self,data_math,data_times,operation_name):
        self.data = data_math
        upper_range = data_math["confidence_interval"] ["upper_range"]
        lower_range = data_math["confidence_interval"] ["lower_range"]
        #print(upper_range)
        #print(lower_range)
        c_lower_range = 0
        c_upper_range = 0
        C_confidence_interval = 0
        mean = data_math["mean"]
        for time in data_times:
            if time < lower_range:
                
                c_lower_range += 1
            elif time > upper_range:
                c_upper_range += 1
            else:
                C_confidence_interval += 1      
        labels = 'confidence_interval','up_confidence_interval','dow_confidence_interval'
        sizes = [C_confidence_interval,c_upper_range,c_lower_range]
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
                shadow=True,startangle = 90 )
        ax1.axis('equal')
        plt.title("Grafico intervalo de confiança" + operation_name)
        plt.show()
        plt.savefig(operation_name+'.png', format='png', bbox_inches='tight')
        plt.close() 

class mean_bar_graphic:
    def __init__(self,means):
        procedures=['times_add_experience',
                    'times_data',
                    'times_adicionar_perfil',
                    'times_all_profile',
                    'times_search_residence',
                    'times_search_user_email_return_inf',
                    'times_search_user_email_return_xp',
                    'times_search_users_course']
        plt.barh(procedures, means, color='green')
        plt.ylabel("Procedures")
        plt.xlabel("Media por Segundo")
        plt.title("medias de tempo de  200 execução dos procedimentos ")
        plt.show()
        plt.savefig('means'+'.png', format='png', bbox_inches='tight')
        plt.close() 

def operation(operation,operation_name,paramenter1=None,paramenter2=None):
    operation = operation
    operation_name = operation_name
    paramenter1 = paramenter1
    paramenter2 = paramenter2
    if paramenter2:
        data_math, data_times = run_analise(operation=operation,
                                            operation_name=operation_name,
                                            parameter1=paramenter1,
                                            parameter2=paramenter2)
        return (data_math, data_times,operation_name)
    else:
        data_math, data_times = run_analise(operation=operation,
                                            operation_name=operation_name,
                                            parameter1=paramenter1)
        return (data_math, data_times,operation_name)
        


data_math1, data_times,operation_name =operation (conection.add_experience,
                                                "add_experience",
                                                "fffff@gmail.com",
                                                "programação em python web")

Pizza_graphic1 = Pizza_graphic(data_math1, data_times,operation_name)

data_math2, data_times,operation_name = operation (conection.data,
                                                "data","email",
                                                "fffff@gmail.com")

Pizza_graphic2 = Pizza_graphic(data_math2, data_times,operation_name)

data_math3, data_times,operation_name = operation(conection.adicionar_perfil,
                                                "adicionar_perfil",
                                                {
                                                    "email": "fabricio@gmail.com",
                                                    "nome": "fabricio",
                                                    "sobrenome": "souza",
                                                    "residencia": "ananideua",
                                                    "formacao academica": [
                                                        "ciencia da computacao"
                                                    ],
                                                    "habilidade": [
                                                        "programação em python"
                                                    ],
                                                    "experiencia": [
                                                        "projeto pessoais em django"
                                                    ]
                                                })
Pizza_graphic3 = Pizza_graphic(data_math3,data_times,operation_name)

data_math4, data_times,operation_name = operation(conection.all_profile,
                                                "all_profile")
Pizza_graphic4 = Pizza_graphic(data_math4,data_times,operation_name)


data_math5, data_times,operation_name = operation(conection.search_residence,
                                                "search_residence","belem")
Pizza_graphic5 = Pizza_graphic(data_math5,data_times,operation_name)

data_math6, data_times,operation_name = operation(conection.search_user_email_return_inf,
                                                "search_user_email_return_inf",
                                                "fffff@gmail.com"
                                                )
Pizza_graphic6 = Pizza_graphic(data_math6,data_times,operation_name)

data_math7, data_times,operation_name = operation (conection.search_user_email_return_xp,
                                                  "search_user_email_return_xp",
                                                  "fffff@gmail.com")
Pizza_graphic7 = Pizza_graphic(data_math7,data_times,operation_name)

data_math8, data_times,operation_name = operation(conection.search_users_course,
                                                "search_users_course",
                                                "ciencia da computacao")
Pizza_graphic8 = Pizza_graphic(data_math8,data_times,operation_name)

def metrica_math(data_math,metrica):
    return(data_math[metrica])

means_metrica = []
metrica = "mean"

means_metrica.append(metrica_math(data_math1,metrica))
means_metrica.append(metrica_math(data_math2,metrica))
means_metrica.append(metrica_math(data_math3,metrica))
means_metrica.append(metrica_math(data_math4,metrica))
means_metrica.append(metrica_math(data_math5,metrica))
means_metrica.append(metrica_math(data_math6,metrica))
means_metrica.append(metrica_math(data_math7,metrica))
means_metrica.append(metrica_math(data_math8,metrica))
mean_bar_graphic = mean_bar_graphic(means_metrica)
print(means_metrica)
