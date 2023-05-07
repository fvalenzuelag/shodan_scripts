import os
import shodan
from dotenv import load_dotenv

load_dotenv()

SHODAN_API_KEY = os.getenv('SHODAN_API_KEY')
api = shodan.Shodan(SHODAN_API_KEY)

QUERY = 'country:"US"'

try:
    results = api.search(QUERY)
    print(f"Total results found: {results['total']}\n")

    # Print information about each device
    for result in results['matches']:
        print(f"IP Address: {result['ip_str']}")

        # Check if the hostnames list is not empty before accessing its first element
        if result.get('hostnames'):
            print(f"Hostname: {result['hostnames'][0]}")
        else:
            print("Hostname: N/A")

        # Print the organization if it exists, otherwise print "N/A"
        print(f"Organization: {result.get('org', 'N/A')}")

        # Check if the ports list is not empty before joining its elements
        if result.get('ports'):
            print(f"Open Ports: {', '.join(str(p) for p in result['ports'])}")
        else:
            print("Open Ports: N/A")

        print()

except shodan.APIError as e:
    print(f"Error: {e}")