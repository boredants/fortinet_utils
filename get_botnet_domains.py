import requests
import warnings
import sys


def main():

    get_botnet_domains()


def get_botnet_domains():
    """Retrieve a list of active botnet domains from a Fortigate firewall
    Update the 'fw' and 'token' variables as appropriate.
    """

    fw = "<HTTPS://YOUR_FORTIGATE_IP:YOUR_FORTIGATE_PORT>"

    path = "/api/v2/monitor/system/botnet-domains/hits/?access_token="

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

        for key in r['results']:
            print()
            for k,v in key.items():
                print("{0:6} :  {1}".format(k.upper(), str(v)))


if __name__ == '__main__':
    main()
