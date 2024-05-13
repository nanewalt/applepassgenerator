from applepassgenerator.client import ApplePassGeneratorClient
from applepassgenerator.models import EventTicket
from applepassgenerator.utils import Barcode, BarcodeFormat
import json

BASE_PATH = 'tests'

team_identifier = "65QNR2XSA2"
pass_type_identifier = "pass.com.opassity.app"
organization_name = "Opassity"

applepassgenerator_client = ApplePassGeneratorClient(
    team_identifier,
    pass_type_identifier,
    organization_name
)

def generate_pass(event, guest):
    # Configure pass content
    card_info = EventTicket()
    card_info.add_header_field("event-start", event.get("start_timestamp"), "START TIME")
    card_info.add_primary_field("event-name", event.get("title"), "EVENT")
    card_info.add_auxiliary_field("location-address", event.get("location").get("address"), "ADDRESS")
    card_info.add_auxiliary_field("location-city", event.get("location").get("city"), "CITY")
    card_info.add_auxiliary_field("location-state", event.get("location").get("state"), "STATE")
    card_info.add_auxiliary_field("location-zip", event.get("location").get("zip"), "ZIP")
    card_info.add_secondary_field("host-name", f"{guest.get('host').get('profile').get('first_name')} {guest.get('host').get('profile').get('last_name')}", "HOST NAME")
    card_info.add_secondary_field("guest-group", guest.get("group"), "GROUP")


    # Configure top level pass
    apple_pass = applepassgenerator_client.get_pass(card_info)
    apple_pass.description = "Opassity Event"
    apple_pass.logo_text = "Opassity"
    apple_pass.background_color = "#F1F1F1"
    apple_pass.label_color = "#F97316"
    payload = {
        "eventId": "a328hasfdala",
        "profileId": "asf22423u9sa8",
        "timestamp": "2024-05-11T12:00:00",
        "group": "VIP"
    }
    apple_pass.barcode = Barcode(json.dumps(payload), BarcodeFormat.QR)

    # Add media files
    apple_pass.add_file("icon.png", open(f"{BASE_PATH}/icon.png", "rb"))
    apple_pass.add_file("logo.png", open(f"{BASE_PATH}/logo.png", "rb"))

    CERTIFICATE_PATH = f"{BASE_PATH}/certs/out/signerCert.pem"
    PASSWORD_KEY = f"{BASE_PATH}/certs/out/signerKey.pem"
    WWDR_CERTIFICATE_PATH = f"{BASE_PATH}/certs/out/wwdr.pem"
    CERTIFICATE_PASSWORD = "test"
    OUTPUT_PASS_NAME = f"{BASE_PATH}/out/test.pkpass"

    apple_pass = apple_pass.create(
        CERTIFICATE_PATH,
        PASSWORD_KEY,
        WWDR_CERTIFICATE_PATH,
        CERTIFICATE_PASSWORD,
        OUTPUT_PASS_NAME
    )

    # return apple_pass.getvalue()


if __name__ == '__main__':
    event = {
        "title": "Test Event",
        "location": {
            "address": "123 Main Street",
            "city": "Los Angeles",
            "state": "CA",
            "zip": "90077"
        },
        "start_timestamp": "2024-05-11T13:30:00",
    }
    guest = {
        "host": {
            "profile": {"first_name": "John", "last_name": "Smith"}
        },
        "group": "VIP"
    }
    generate_pass(event, guest)
