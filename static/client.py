from two1.commands.config import Config
from two1.lib.wallet import Wallet
from two1.lib.bitrequests import BitTransferRequests

import sys

wallet = Wallet()
username = Config().username
requests = BitTransferRequests(wallet, username)

keys = ['a', 'b', 'up', 'down', 'left', 'right', 'start', 'select']

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print('Usage: python3 client.py <server>')
  server_url = 'http://{}'.format(sys.argv[1])

  while(True):
    key = input('Button ({})? '.format('/'.join(keys)))

    if key not in keys:
      print('Invalid button')
    else:
      req_url = '{}/press/{}'.format(server_url, key)
      answer = requests.get(url=req_url)

      if answer.status_code != 200:
        print("Could not make payment.")

