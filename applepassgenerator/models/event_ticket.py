from applepassgenerator.models.base import PassInformation

class EventTicket(PassInformation):
    def __init__(self):
        super(EventTicket, self).__init__()
        self.jsonname = "eventTicket"


