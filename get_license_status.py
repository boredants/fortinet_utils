import requests
import warnings
import sys


def main():

    get_rate_based_sigs()


def get_rate_based_sigs():
    """Retrieve comprehensive licensing info from a Fortigate
    Update the 'fw' and 'token' variables as appropriate.
    """

    fw = "<<HTTPS://YOUR_FORTIGATE_IP:YOUR_FORTIGATE_PORT>>"

    path = "/api/v2/monitor/license/status/select/?access_token="

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

        #This looks nasty but it's dealing with a dictionary of dictionaries possibly consisting of other dictionaries...
        # {key:{key:{key:value},{key:value}}}        
        for i in (r['results']):
            print()
            print(i.upper() + ":")
            for k,v in r['results'][i].items():
                if isinstance(v, dict):
                    pad = ' ' * 4
                    print(pad + k.upper() + ":")
                    for c,d in v.items():
                        if isinstance(d, dict):
                            pad = ' ' * 6
                            print(pad + c.upper() + ":")
                            for e,f in dict(d).items():
                                pad = ' ' * 8
                                print(pad + e.upper() + " : " + str(f))
                        else:
                            pad = ' ' * 6
                            print(pad + c.upper() + " : " + str(d))
                else:
                    pad = ' ' * 2
                    print(pad + k.upper() + " : " + str(v))

        
         
if __name__ == '__main__':
    main()
