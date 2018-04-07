import socket
from urllib import parse
import json

from game.server.controller import Controller


class OXServer:
    TCP_IP = '127.0.0.1'
    TCP_PORT = 5005
    BUFFER_SIZE = 1024
    controller = Controller()

    def _bind_and_listen(self):
        s = None
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((self.TCP_IP, self.TCP_PORT))
            s.listen(8)
        except:
            s = None
        if s is None:
            print('Could not open socket')
            exit(1)
        return s

    def generate_response(self, status_code, body_return_value):
        if (status_code == 200):
            return_dict = {"Headers": {"Status": status_code}, "Payload": {"Result": body_return_value}}
        else:
            return_dict = {"Headers": {"Status": status_code}, "Payload": {"Error Message": "Not found"}}
        return json.dumps(return_dict)

    def _parse_query(self, data):
        """
            Parse request parameters
            if this function raises KeyError
            the main server loop closes the connection automatically
        """
        data_str = data.decode(encoding='ascii')
        request_params_list = parse.parse_qsl(data_str)
        if request_params_list[0][0] != 'method' or request_params_list[1][0] != 'id':
            raise ValueError('Query string does not include method and id at the beginning')
        method = request_params_list[0][1]
        game_id = request_params_list[1][1]
        optional_params_list = [value for key, value in request_params_list[2:]]
        return method, game_id, optional_params_list

    def run(self):
        s = self._bind_and_listen()

        # server loop
        while True:
            conn = addr = None
            try:
                # accept next connection
                conn, addr = s.accept()

                # get data from the client
                data = conn.recv(self.BUFFER_SIZE)  # constant BUFFER_SIZE for GET requests prevents simple DoS attacks
                if not data:
                    continue

                # call the controller get method
                action, game_id, optional_params = self._parse_query(data)
                ret = self.controller.get(action, game_id, *optional_params)

                # on failure return empty response to the client
                # it would be much better to use HTTP instead of sock library
                # and return standard status codes like 200 or 404 to the client
                if ret is None:
                    json_ret = self.generate_response(404, "")
                else:
                    json_ret = self.generate_response(200, ret)
                conn.sendall(str(json_ret).encode())
            except Exception as e:
                # log exception and client address
                print(e)
                print('Request error from:')
                print(addr)
            finally:
                conn.close()
                # print('Games active: ' + str(self.controller.games_active()))
        s.close()  # this line should remain here in the case of using os signals to close the server process


if __name__ == '__main__':
    OXServer().run()
