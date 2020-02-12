import requests
import warnings
import sys
from datetime import date as d

def main():

    backup()


def backup():
    """Back up the Fortigate config to a file
    Update the 'fw' and 'token' variables as appropriate.
    """

    fw = "<HTTPS://YOUR_FORTIGATE_IP:YOUR_FORTIGATE_PORT>"

    path = "/api/v2/monitor/system/config/backup/"

    token = "<YOUR_API_KEY>"

    params = {'scope': 'global'}

    headers = {'Authorization': f'Bearer {token}'}

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        
        with open("fortigate_backup_" + d.today().strftime("%Y%m%d") + ".conf", 'w') as f:

            try:
                r = requests.get(fw + path, headers=headers, params=params, verify=False)
            except Exception:
                print("Something went wrong.  Is the url correct?  Exiting...")
                sys.exit()

            for line in r.text.split('\n'):
                print(line, file=f)


if __name__ == '__main__':
    main()
