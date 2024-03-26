from PySide6.QtNetwork import QTcpSocket

import json

class TerminalConnectionServer():
    def __init__(self, socket_instance, gui_instance):
        
        self.socket = socket_instance
        self.socket.readyRead.connect(self.respond)
        self.socket.stateChanged.connect(self.state_change)

        print('descriptor:', self.socket.socketDescriptor())

        # i want to use it for function handling, but i should probably use signals instead?
        self.gui_instance = gui_instance
        self.configured = False

    def respond(self):
        if not self.configured:
            self.first_config()
            self.configured = True

    def first_config(self):
        data = self.socket.readAll().toStdString()
        try:
            request = json.loads(data)
        except Exception as e:  # @todo: add correct except here
            print("Error in json - if this happens because all wasn't sent at once and we started read, we need to change our code to make sure this doesnt't happen, i think.")  # @debug statement
            print(e)
            return

        instance_name = request.get('instance_name')
        print(request)
        instance = self.gui_instance.instances_dict.get(instance_name)
        for key in self.gui_instance.instances_dict:
            print(key)
        print(instance_name)
        instance.signal.ready_read.connect(self.output_to_socket)

        if not instance.loaded:
            instance.open()  # @todo: change to start or something

        self.instance = instance

        self.socket.write(self.instance.output.encode())


    def output_to_socket(self):
        data = self.instance.output_stdout + self.instance.output_stderr
        self.socket.write(data.encode())
        

    def state_change(self):
        if self.socket.state() == QTcpSocket.SocketState.UnconnectedState:
            pass  # @todo: uhm, what do we do here? ... we don't have to use it anymore, right?
