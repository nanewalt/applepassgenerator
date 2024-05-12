from applepassgenerator.models.base import PassInformation

class StoreCard(PassInformation):
    def __init__(self):
        super(StoreCard, self).__init__()
        self.jsonname = "storeCard"

