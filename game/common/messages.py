from urllib import parse
import json


class Messages:
    def __init__(self, game_type):
        self._game_type = '_' + game_type

    def create_request(self, method, game_id, **args):
        return {'method': method + self._game_type, 'id': game_id, **args}

    @staticmethod
    def generate_response(status_code, body_return_value):
        if status_code == 200:
            return_dict = {"Headers": {"Status": status_code}, "Payload": {"Result": body_return_value}}
        else:
            return_dict = {"Headers": {"Status": status_code}, "Payload": {"Error Message": "Not found"}}
        return json.dumps(return_dict)

    @staticmethod
    def parse_incoming_request(data):
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

    @staticmethod
    def prepare_response(response):
        """
         on failure return empty response to the client
         it would be much better to use HTTP instead of sock library
         and return standard status codes like 200 or 404 to the client
         this function mimics that behavior
         """
        if response is None:
            json_ret = Messages.generate_response(404, "")
        else:
            json_ret = Messages.generate_response(200, response)
        return json_ret

    @staticmethod
    def url_encode_request(request):
        return parse.urlencode(request)

    @staticmethod
    def process_response(data):
        data_dict = json.loads(data)
        if data_dict.get("Headers").get("Status") == 404:
            response = None
        else:
            response = data_dict.get("Payload").get("Result")
        return response
