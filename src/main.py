import requests
import json
from pprint import pprint

if __name__ == '__main__':
    print("hello world!")

    # Random jet: AA8A8A
	# https://globe.adsb.one/
	# curl https://api.adsb.one/v2/hex/AA8A8A

    jet = "AA8A8A"

    r = requests.get(f"https://api.adsb.one/v2/hex/{jet}")

    data = json.loads(r.text)['ac']

    pprint(data[0])
    