from PySide6.QtNetwork import QTcpSocket
from CogDirectoryManager import CogDirManager

import json

# optional methods to maybe implement in the future:
# * add_cog
# * stop_instance

# @todo: It seems it's all correct, but I need to do better testing, maybe write some tests too since its easy. Also, there's spec to read to verify its all good - https://www.jsonrpc.org/specification

class RPCResolver():
    def __init__(self, socket_instance, gui_instance):
        
        self.socket = socket_instance
        self.socket.readyRead.connect(self.respond)
        self.socket.stateChanged.connect(self.state_change)

        # @todo: We use it for function calls, but maybe we should use signals instead? Probably not, since you would have to connect them for every new RPCResolver.. And other stuff.
        self.gui_instance = gui_instance

    def respond(self):
        data = self.socket.readAll().toStdString()
        try:
            rpc_request = json.loads(data)
        except Exception as e:  # @todo: add correct except here
            print("Error in json - if this happens because all wasn't sent at once and we started read, we need to change our code to make sure this doesnt't happen, i think.")  # @debug statement
            print(e)
            response = { 'jsonrpc': '2.0', 'error': { 'code': -32700, 'message': f'Invalid JSON was received by the server.'}, 'id': None }
            self.socket.write(json.dumps(response, indent=2).encode())
            return

        if rpc_request.get('jsonrpc') == None:
            response = { 'jsonrpc': '2.0', 'error': { 'code': -32600, 'message': f'Invalid Request - missing jsonrpc field.'}, 'id': None }
            self.socket.write(json.dumps(response, indent=2).encode())
            return

        if rpc_request.get('method') == None:
            response = { 'jsonrpc': '2.0', 'error': { 'code': -32600, 'message': f'Invalid Request - missing method field.'}, 'id': None }
            self.socket.write(json.dumps(response, indent=2).encode())
            return

        if rpc_request.get('id') == None:  # requests without id are 'notifications', after sending them client does not wait for a response
            return

        if rpc_request['method'] == 'list_instances':
            instances = {}
            for instance in self.gui_instance.instances:
                instances[instance.name] = {
                    'name': instance.name, 
                    'version': instance.version, 
                    'token': instance.token, 
                    'is_running': instance.loaded
                }

            response = {'jsonrpc': '2.0', 'result': instances, 'id': rpc_request['id']}
            self.socket.write(json.dumps(response, indent=2).encode())
            return


        if rpc_request['method'] == 'start_instance':
            wrong_instances = []
            for instance_name in rpc_request['params']:
                instance = self.gui_instance.instances_dict.get(instance_name)
                if instance == None:
                    wrong_instances.append(instance_name)
                    continue
                instance.open()  # @todo: we may want to change it to actual start() method

            if len(wrong_instances) == 0:
                response = {'jsonrpc': '2.0', 'result': 'Finished with success.', 'id': rpc_request['id']}
            else:
                response = {
                    'jsonrpc': '2.0', 
                    'error': { 'code': -32602, 'message': f'Instances {wrong_instances} do not exist.'}, 
                    'id': rpc_request['id']
                }

            self.socket.write(json.dumps(response, indent=2).encode())
            return


        if rpc_request['method'] == 'list_cogs':
            response = {'jsonrpc': '2.0', 'result': CogDirManager.get_cogs(), 'id': rpc_request['id']}
            self.socket.write(json.dumps(response, indent=2).encode())
            return

            
        if rpc_request['method'] == 'reload_cog':
            instance_name = rpc_request['params'].get('instance_name')
            cog_path = rpc_request['params'].get('cog_path')

            if instance_name == None or cog_path == None:
                response = {
                    'jsonrpc': '2.0', 
                    'error': { 'code': -32602, 'message': f'You have to specify instance_name and cog_path fields in params object.'}, 
                    'id': rpc_request['id']
                }
                self.socket.write(json.dumps(response, indent=2).encode())
                return

            instance = self.gui_instance.instances_dict.get(instance_name)

            # @todo: should we open it, or just start? also, this doesnt work when instance was not loaded..
            if not instance.loaded:
                instance.open()

            # @todo: maybe this is not how it should work, or maybe we should support adding cog paths
            if cog_path not in CogDirManager.get_cogs():
                response = {
                    'jsonrpc': '2.0', 
                    'error': { 'code': -32602, 'message': f'Cog path {cog_path} not added.'}, 
                    'id': rpc_request['id']
                }
                self.socket.write(json.dumps(response, indent=2).encode())
                return

            if instance == None:
                response = {
                    'jsonrpc': '2.0', 
                    'error': { 'code': -32602, 'message': f'Instance {instance_name} not found.'}, 
                    'id': rpc_request['id']
                }
                self.socket.write(json.dumps(response, indent=2).encode())
                return

            # @todo: use signals instead of this or something, whatever, but first make reload_cog non-blocking
            instance.reload_cog(cog_path)
            
            response = {'jsonrpc': '2.0', 'result': 'finished with success', 'id': rpc_request['id']}
            self.socket.write(json.dumps(response, indent=2).encode())
            return

        response = { 'jsonrpc': '2.0', 'error': { 'code': -32601, 'message': f'Method {rpc_request["method"]} not found.'}, 'id': None }
        self.socket.write(json.dumps(response, indent=2).encode())


    def state_change(self):
        if self.socket.state() == QTcpSocket.SocketState.UnconnectedState:
            pass  # @todo: uhm, what do we do here? ... we don't have to use it anymore, right?
