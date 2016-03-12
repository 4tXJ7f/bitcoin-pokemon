from flask import Flask
from flask import make_response
from flask import redirect
from flask import render_template

from two1.lib.wallet import Wallet
from two1.lib.bitserv.flask import Payment

import autopy3
import time

app = Flask(__name__, static_url_path='')
wallet = Wallet()
payment = Payment(app, wallet)

key_map = {
    'a': u'a',
    'b': u'b',
    'up': u'u',
    'down': u'd',
    'left': u'l',
    'right': u'r',
    'start': u's',
    'select': u'e',
}

@app.route('/press/<key>')
@payment.required(10)
def press(key):
  print(key)
  if key in key_map:
    autopy3.key.toggle(key_map[key], True)
    time.sleep(0.2)
    autopy3.key.toggle(key_map[key], False)
  return make_response(redirect('/', code=302))

@app.route('/')
def main():
  return render_template('main.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
