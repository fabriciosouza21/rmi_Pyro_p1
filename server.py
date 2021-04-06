import time
import json
import Pyro4
import threading
from repositorio import RepositorioProfessionalProfile

@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class Interface(object):
    def data(self, field, search):
        profissionalProfile = RepositorioProfessionalProfile()

        users = profissionalProfile.find(field, search)

        return users

class Server():
    def enable(self):
        #Pyro4.Daemon.serveSimple({Interface: "server.interface"}, ns = True)
        self.daemon = Pyro4.Daemon(port=52119)
        uri = self.daemon.register(Interface, "interface") #Registra um objeto Pyro
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
