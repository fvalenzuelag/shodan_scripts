import os
import shodan
from dotenv import load_dotenv

load_dotenv()

SHODAN_API_KEY = os.getenv('SHODAN_API_KEY')
api = shodan.Shodan(SHODAN_API_KEY)

QUERY = 'port:3389'

# Search for devices with the Heartbleed vulnerability
try:
    results = api.search(QUERY)
    print(f"Total results found: {results['total']}\n")

    # Print information about each device
    for result in results['matches']:
        print(f"IP Address: {result['ip_str']}")

except shodan.APIError as e:
    print(f"Error: {e}")