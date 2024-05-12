from applepassgenerator.client import ApplePassGeneratorClient
from applepassgenerator.models import EventTicket

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
    card_info = EventTicket()
    card_info.add_primary_field("event", event.get("title"), "EVENT")
    card_info.add_secondary_field("loc", event.get("location").get("address"), "LOCATION")

    apple_pass = applepassgenerator_client.get_pass(card_info)

    # Add media files
    apple_pass.add_file("icon.png", open(f"{BASE_PATH}/icon.png", "rb"))

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

    print("APPLE_PASS", apple_pass)
    # return apple_pass.getvalue()


if __name__ == '__main__':
    event = {
        "title": "Test Event",
        "location": {
            "address": "123 Main Street"
        },
    }
    guest = {
        
    }
    generate_pass(event, guest)
