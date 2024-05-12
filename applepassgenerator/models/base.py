from applepassgenerator.utils import Field

class PassInformation(object):
    def __init__(self):
        self.header_fields = []
        self.primary_fields = []
        self.secondary_fields = []
        self.back_fields = []
        self.auxiliary_fields = []

    def add_header_field(self, key, value, label):
        self.header_fields.append(Field(key, value, label))

    def add_primary_field(self, key, value, label):
        self.primary_fields.append(Field(key, value, label))

    def add_secondary_field(self, key, value, label):
        self.secondary_fields.append(Field(key, value, label))

    def add_back_field(self, key, value, label):
        self.back_fields.append(Field(key, value, label))

    def add_auxiliary_field(self, key, value, label):
        self.auxiliary_fields.append(Field(key, value, label))

    def json_dict(self):
        d = {}
        if self.header_fields:
            d.update({"headerFields": [f.json_dict() for f in self.header_fields]})
        if self.primary_fields:
            d.update({"primaryFields": [f.json_dict() for f in self.primary_fields]})
        if self.secondary_fields:
            d.update(
                {"secondaryFields": [f.json_dict() for f in self.secondary_fields]}
            )
        if self.back_fields:
            d.update({"backFields": [f.json_dict() for f in self.back_fields]})
        if self.auxiliary_fields:
            d.update(
                {"auxiliaryFields": [f.json_dict() for f in self.auxiliary_fields]}
            )
        return d

