from re import findall
import Pyro4
import threading
from repositorio import RepositorioProfessionalProfile


@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class Interface(object):
    def __init__(self):
        self.profiles = RepositorioProfessionalProfile()

    def data(self, field, search):

        if field != None and search != None:
            users = self.profiles.find(field, search)
        else:
            users = self.profiles.find_all()

        return users

    def search_users_course(self, search):
        return (self.profiles.find('formacao academica', search))

    def search_user_email_return_xp(self, search):
        # print(search)
        experiencia = []
        users = self.profiles.find('email', search)
        for user in users:
            experiencia.append(user['experiencia'])

        # print(experiencia)
        return (experiencia)

    def search_user_email_return_inf(self, search):
        return self.profiles.find('email', search)

    def adicionar_perfil(self, profile):
        self.profiles.save(profile)

    def search_residence(self, search):
        return self.profiles.find("residencia", search)

    def add_experience(self, email, experiencia):
        user = self.profiles.findUser(email)
        user["experiencia"].append(experiencia)

    def all_profile(self):
        profiles = self.profiles.find_all()
        return profiles


class Server():
    def enable(self):
        # Pyro4.Daemon.serveSimple({Interface: "server.interface"}, ns = True)
        #self.daemon = Pyro4.Daemon(port=52119)
        # Registra um objeto Pyro
        #uri = self.daemon.register(Interface, "interface")
        self.daemon = Pyro4.Daemon(host='10.0.0.182',port=52119)
        self.ns = Pyro4.locateNS()
        self.uri = self.daemon.register(Interface)
        self.ns.register('example.interface',self.uri)
        self.thread = threading.Thread(target=self.daemonLoop)
        self.thread.start()
        print("Started thread")
        #print('uri: ', uri)
        #ns.register("serv.teste", uri)

    def disable(self):
        print("Called for daemon shutdown")
        self.daemon.shutdown()

    def daemonLoop(self):
        self.daemon.requestLoop()
        print("Daemon has shut down no prob")


def main():
    server = Server()

    server.enable()
    server.daemonLoop()


if __name__ == '__main__':
    main()
