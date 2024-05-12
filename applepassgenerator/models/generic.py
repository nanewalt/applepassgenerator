from applepassgenerator.models.base import PassInformation

class Generic(PassInformation):
    def __init__(self):
        super(Generic, self).__init__()
        self.jsonname = "generic"


