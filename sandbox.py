import requests
import json

# Disable warnings for self-signed certificates
requests.packages.urllib3.disable_warnings()

# Configuration
# URL = "https://ios-xe-mgmt.cisco.com:9443/restconf/data/ietf-interfaces:interfaces"
# URL = "https://sandbox-iosxe-recomm-1.cisco.com:443/restconf/data/ietf-interfaces:interfaces"
URL = "http://127.0.0.1:8000/interfaces/"
USERNAME = "developer"
PASSWORD = "C1sco12345"

HEADERS = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json",
}


def create_payload(interface_number: int) -> dict:
    """
    Creates the payload for the loopback interface.
    
    Args:
        interface_number (int): The loopback interface number.
        
    Returns:
        dict: The payload as a dictionary.
    """
    # ip_address = f"1.2.3.{interface_number}"
    # return {
    #     "ietf-interfaces:interface": {
    #         "name": f"Loopback123{interface_number}",
    #         "description": "Added with RESTCONF",
    #         "type": "iana-if-type:softwareLoopback",
    #         "enabled": True,
    #         "ietf-ip:ipv4": {
    #             "address": [
    #                 {
    #                     "ip": ip_address,
    #                     "netmask": "255.255.255.255",
    #                 }
    #             ]
    #         },
    #     }
    # }
    ip_address = f"1.2.3.{interface_number}"
    return {
            "name": f"LoopBack{interface_number}",
            "description":"Configured by DEVNET",
            "type": "iana-if-type:ethernetCsmacd",
            "enable": True,
            "ietf_ip": {
                "address": [
                {
                    "ip": ip_address,
                    "netmask": "255.255.255.255"
                }
                ]
            }
        }



def configure_loopbacks(total_interfaces: int):
    """
    Configures loopback interfaces using RESTCONF.
    
    Args:
        total_interfaces (int): Number of loopback interfaces to configure.
    """
    for interface_number in range(total_interfaces):
        payload = create_payload(interface_number)
        print(f"Creating Loopback Interface: Loopback123{interface_number}")
        
        response = requests.post(
            URL,  
            data=json.dumps(payload), 
            verify=False,
        )
        
        # Print response details
        if response.status_code == 201:
            print(f"Successfully created Loopback123{interface_number}")
        else:
            print(f"Failed to create Loopback123{interface_number}")
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}\n")

if __name__ == "__main__":
    try:
        TOTAL_INTERFACES = 5  # Number of loopbacks to configure
        configure_loopbacks(TOTAL_INTERFACES)
    except Exception as e:
        print(f"An error occurred: {e}")
