import requests
import warnings
import sys


def main():

    get_routes()


def get_routes():
    """Retrieve a list of all active IPv4 routing table entries
    Update the 'fw' and 'token' variables as appropriate.
    """

    fw = "<<HTTPS://YOUR_FORTIGATE_IP:YOUR_FORTIGATE_PORT>>"

    # Change ipv4 to ipv6 here to get active ipv6 routes
    path = "/api/v2/monitor/router/ipv4/select/?access_token="

    token = "<YOUR_API_KEY>"

    content_filter = ""

    if content_filter != "":
        url = fw + path + token + content_filter
    else:
        url = fw + path + token

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        
        try:
            r = requests.get(url, verify=False).json()
        except Exception:
            print("Something went wrong.  Is the url correct?  Exiting...")
            sys.exit()
        
        active_routes = []

        for i in (r['results']):
            if i['ip_mask'] not in active_routes:
                active_routes.append(i['ip_mask'])

        for route in active_routes:
            print(route)

if __name__ == '__main__':
    main()
