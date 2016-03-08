from two1.commands.config import Config
from two1.lib.wallet import Wallet
from two1.lib.bitrequests import BitTransferRequests

wallet = Wallet()
username = Config().username
requests = BitTransferRequests(wallet, username)

if __name__ == '__main__':
  server_url = sys.argv[1]
  key = sys.argv[2]
  sel_url = server_url+'/press/{1}'
  answer = requests.get(url=sel_url.format(int(pic_num), wallet.get_payout_address()), stream=True)

  if answer.status_code != 200:
    print("Could not make payment.")
