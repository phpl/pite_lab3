import json
import socket
from urllib import parse

from game.server.OXServer import OXServer


class OXControllerNetworkClient:
    TCP_IP = '127.0.0.1'
    TCP_PORT = OXServer.TCP_PORT
    BUFFER_SIZE = OXServer.BUFFER_SIZE

    def get(self, **params):
        query_str = parse.urlencode(params)
        request_not_completed = True
        return_val = s = None
        while request_not_completed:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((self.TCP_IP, self.TCP_PORT))
                s.send(query_str.encode())
                data = s.recv(self.BUFFER_SIZE).decode(encoding='UTF-8')
                data_dict = json.loads(data)
                if data_dict.get("Headers").get("Status") == 404:
                    return_val = None
                else:
                    return_val = data_dict.get("Payload").get("Result")
                request_not_completed = False
            except:
                print('Error: Cannot connect to the server!')
                try_again = input('Do you want to try again? Please press enter to confirm or type N to exit.\n')
                if len(try_again) > 0:
                    exit(1)
                print('Please wait...')
            finally:
                s.close()
        return return_val
