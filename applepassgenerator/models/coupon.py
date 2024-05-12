from applepassgenerator.models.base import PassInformation

class Coupon(PassInformation):
    def __init__(self):
        super(Coupon, self).__init__()
        self.jsonname = "coupon"


