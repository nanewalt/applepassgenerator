from applepassgenerator.models.base import PassInformation

class TransitType:
    AIR = "PKTransitTypeAir"
    TRAIN = "PKTransitTypeTrain"
    BUS = "PKTransitTypeBus"
    BOAT = "PKTransitTypeBoat"
    GENERIC = "PKTransitTypeGeneric"


class BoardingPass(PassInformation):
    def __init__(self, transit_type=TransitType.AIR):
        super(BoardingPass, self).__init__()
        self.transit_type = transit_type
        self.jsonname = "boardingPass"

    def json_dict(self):
        d = super(BoardingPass, self).json_dict()
        d.update({"transitType": self.transit_type})
        return d

