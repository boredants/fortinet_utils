import requests
import warnings
import sys


def main():

    get_rate_based_sigs()


def get_rate_based_sigs():
    """Retrieve a list of rate-based IPS signatures from the Fortigate
    Update the 'fw' and 'token' variables as appropriate.
    """

    fw = "<<HTTPS://YOUR_FORTIGATE_IP:YOUR_FORTIGATE_PORT>>"

    path = "/api/v2/monitor/ips/rate-based/select/?access_token="

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
                
        for i in (r['results']):
            #print(r['results'][i]['name']) - print a single key without the loop
            print("{0:14}: {1}".format("NAME",i['name']))
            print("{0:14}: {1}".format("ID",str(i['id'])))
            print("{0:14}: {1}".format("RATE-COUNT",str(i['rate-count'])))
            print("{0:14}: {1}".format("RATE-DURATION",str(i['rate-duration']) + "\n"))

        # Another way, with slightly less output control
        # for key in r['results']:
        #     print()  
        #     for k,v in key.items():
        #         print("{0:13} :  {1}".format(k.upper(), str(v)))

if __name__ == '__main__':
    main()
