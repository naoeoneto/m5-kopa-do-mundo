class NegativeTitlesError(Exception):
    def __init__(self, message, status):
        self.message = message
        self.status = 400


class InvalidYearCupError(Exception):
    def __init__(self, message):
        self.message = message


class ImpossibleTitlesError(Exception):
    def __init__(self, message):
        self.message = message
