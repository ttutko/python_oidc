from keycloak import KeycloakOpenID
import pprint

keycloak_openid = KeycloakOpenID(server_url="https://localhost:8181/auth/",
    client_id="example_client",
    realm_name="example_realm",
    client_secret_key="0f0f6195-41bb-4077-bd30-469964328ba0",
    verify=False)

config_well_know = keycloak_openid.well_know()

token = keycloak_openid.token("example_client", "0f0f6195-41bb-4077-bd30-469964328ba0", grant_type="client_credentials")

pprint.pprint(token)

