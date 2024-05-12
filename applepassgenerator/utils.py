class Alignment:
    LEFT = "PKTextAlignmentLeft"
    CENTER = "PKTextAlignmentCenter"
    RIGHT = "PKTextAlignmentRight"
    JUSTIFIED = "PKTextAlignmentJustified"
    NATURAL = "PKTextAlignmentNatural"


class BarcodeFormat:
    PDF417 = "PKBarcodeFormatPDF417"
    QR = "PKBarcodeFormatQR"
    AZTEC = "PKBarcodeFormatAztec"
    CODE128 = "PKBarcodeFormatCode128"


class DateStyle:
    NONE = "PKDateStyleNone"
    SHORT = "PKDateStyleShort"
    MEDIUM = "PKDateStyleMedium"
    LONG = "PKDateStyleLong"
    FULL = "PKDateStyleFull"


class NumberStyle:
    DECIMAL = "PKNumberStyleDecimal"
    PERCENT = "PKNumberStylePercent"
    SCIENTIFIC = "PKNumberStyleScientific"
    SPELLOUT = "PKNumberStyleSpellOut"


class Field(object):
    def __init__(self, key, value, label=""):
        self.key = key  # Required. The key must be unique within the scope
        self.value = value  # Required. Value of the field. For example, 42
        self.label = label  # Optional. Label text for the field.
        self.changeMessage = ""  # Optional. Format string for the alert text that is displayed when the pass is updated
        self.textAlignment = Alignment.LEFT

    def json_dict(self):
        return self.__dict__


class DateField(Field):
    def __init__(
        self,
        key,
        value,
        label="",
        date_style=DateStyle.SHORT,
        time_style=DateStyle.SHORT,
        ignores_time_zone=False,
    ):
        super(DateField, self).__init__(key, value, label)
        self.dateStyle = date_style  # Style of date to display
        self.timeStyle = time_style  # Style of time to display
        self.isRelative = (
            False  # If true, the labels value is displayed as a relative date
        )
        if ignores_time_zone:
            self.ignoresTimeZone = ignores_time_zone

    def json_dict(self):
        return self.__dict__


class NumberField(Field):
    def __init__(self, key, value, label=""):
        super(NumberField, self).__init__(key, value, label)
        self.numberStyle = NumberStyle.DECIMAL  # Style of date to display

    def json_dict(self):
        return self.__dict__


class CurrencyField(NumberField):
    def __init__(self, key, value, label="", currency_code=""):
        super(CurrencyField, self).__init__(key, value, label)
        self.currencyCode = currency_code  # ISO 4217 currency code

    def json_dict(self):
        return self.__dict__


class Barcode(object):
    def __init__(
        self,
        message,
        format=BarcodeFormat.PDF417,
        alt_text="",
        message_encoding="iso-8859-1",
    ):
        self.format = format
        self.message = (
            message  # Required. Message or payload to be displayed as a barcode
        )
        self.messageEncoding = message_encoding  # Required. Text encoding that is used to convert the message
        if alt_text:
            self.altText = alt_text  # Optional. Text displayed near the barcode

    def json_dict(self):
        return self.__dict__


class Location(object):
    def __init__(self, latitude, longitude, altitude=0.0):
        # Required. Latitude, in degrees, of the location.
        try:
            self.latitude = float(latitude)
        except (ValueError, TypeError):
            self.latitude = 0.0
        # Required. Longitude, in degrees, of the location.
        try:
            self.longitude = float(longitude)
        except (ValueError, TypeError):
            self.longitude = 0.0
        # Optional. Altitude, in meters, of the location.
        try:
            self.altitude = float(altitude)
        except (ValueError, TypeError):
            self.altitude = 0.0
        # Optional. Notification distance
        self.distance = None
        # Optional. Text displayed on the lock screen when
        # the pass is currently near the location
        self.relevantText = ""

    def json_dict(self):
        return self.__dict__

