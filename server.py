import Pyro4
import threading
from repositorio import RepositorioProfessionalProfile


@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class Interface(object):
    def __init__(self):
        self.profiles = RepositorioProfessionalProfile()

    def data(self, field, search):
        profissionalProfile = RepositorioProfessionalProfile()

        if field != None and search != None:
            users = profissionalProfile.find(field, search)
        else:
            users = profissionalProfile.find_all()

        return users

    def adicionar_perfil(self, profile):
        self.profiles.save(profile)

    def search_residence(self, search):
        return self.profiles.find("residencia", search)


class Server():
    def enable(self):
        # Pyro4.Daemon.serveSimple({Interface: "server.interface"}, ns = True)
        self.daemon = Pyro4.Daemon(port=52119)
        # Registra um objeto Pyro
        uri = self.daemon.register(Interface, "interface")
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
