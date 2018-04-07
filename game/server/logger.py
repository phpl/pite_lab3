class Logger:
    @staticmethod
    def log_request(e, address):
        print('Log: ' + str(e) + ', Request error from:' + str(address))

    @staticmethod
    def log(message):
        print('Log: ' + str(message))
