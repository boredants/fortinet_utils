import requests
import warnings
import sys


def main():

    get_ip_objects()


def get_ip_objects():
    """Retrieve a list of all the IP address objects on a Fortigate firewall
    Update the 'fw' and 'token' variables as appropriate.
    """

    fw = "<HTTPS://YOUR_FORTIGATE_IP:YOUR_FORTIGATE_PORT>"

    path = "/api/v2/cmdb/firewall/address/?access_token="

    token = "<YOUR_API_KEY>"

    content_filter = "&format=start-ip"

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

    ip_list = []
    for key in r['results']:
        for k,v in key.items():
            ip_list.append(v)

    sorted_list = []
    for ip in sorted(ip_list, key= lambda ip: (int(ip.split('.')[0]),
                                              (int(ip.split('.')[1]),
                                              (int(ip.split('.')[2]),
                                              (int(ip.split('.')[3])))))):
        
        if ip not in sorted_list:
            sorted_list.append(ip)

    for ip in sorted_list:
        print(ip)


if __name__ == '__main__':
    main()
