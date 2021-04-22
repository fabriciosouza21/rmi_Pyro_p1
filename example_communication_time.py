from os import times
from repositorio import A
from communication_time import communication_time
import Pyro4
conection = Pyro4.Proxy("PYRO:interface@localhost:52119")

operation_name = "search_users_course"
course = "ciencia da computacao"
call_pyro = conection.search_users_course
times_search_course = communication_time(operation_name=operation_name,
                                         operation=call_pyro)
A = times_search_course.run(parameter1=course)
