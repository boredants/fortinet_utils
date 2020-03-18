import requests
import warnings
import sys


def main():

    print("\n########################################")
    print("# CURRENTLY CONNECTED SSL VPN TUNNELS: #")
    print("########################################\n")

    get_ssl_vpn()


def get_ssl_vpn():
    """Get a list of active ssl vpn tunnels
    Update the 'fw' and 'token' variables as appropriate.
    """

    fw = "<<HTTPS://YOUR_FORTIGATE_IP:YOUR_FORTIGATE_PORT>>"

    path = "/api/v2/monitor/vpn/ssl/select/?access_token="

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

        for i in r['results']:
            print("{0:14} : {1}".format("USERNAME", i['user_name']))
            print("{0:14} : {1}".format("LOGIN TIME", i['last_login_time']))
            print("{0} : {1}".format("REMOTE ADDRESS", i['remote_host']))
            print("{0:14} : {1}".format("TIMESTAMP", i['last_login_timestamp']))
            if not i['subsessions']:
                print()
            else:
                print("{0} : {1}".format("TUNNEL ADDRESS", i['subsessions'][0]['aip']))
                print("{0:14} : {1}".format("BYTES IN", i['subsessions'][0]['in_bytes']))
                print("{0:14} : {1}\n".format("BYTES OUT", i['subsessions'][0]['out_bytes']))
  

if __name__ == '__main__':
    main()
