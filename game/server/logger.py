class Logger:
    @staticmethod
    def log(e, address):
        print('Log: ' + str(e) + ', Request error from:' + str(address))

    @staticmethod
    def log(message):
        print('Log: ' + str(message))
