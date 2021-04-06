import Pyro4
import threading
import time

@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class Interface(object):
    def test(self):
        res = "test_string"
        print("Test returning:"+res)
        return res
class Server():
    def enable(self):
        self.daemon = Pyro4.Daemon(port=53546)
        uri = self.daemon.register(Interface, "interface")
        '''self.thread = threading.Thread(target=self.daemonLoop)
        self.thread.start()
        print("Started thread")'''
        print('uri: ', uri)

    def disable(self):
        print("Called for daemon shutdown")
        self.daemon.shutdown()

    def daemonLoop(self):
        self.daemon.requestLoop()
        print("Daemon has shut down no prob")

server = Server()
interface = Interface()

server.enable()
server.daemonLoop()
