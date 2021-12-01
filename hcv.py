import base64
import json
import os

try:
    from urllib.error import HTTPError, URLError
    from urllib.request import urlopen
except ImportError:
    from urllib2 import HTTPError, URLError
    from urllib2 import urlopen


DEFAULT_VAULT_ADDR = "https://127.0.0.1:8200"


class Client:
    def __init__(self, addr="", token=""):
        self.addr = addr or os.getenv("VAULT_ADDR", DEFAULT_VAULT_ADDR)
        self.token = token or os.getenv("VAULT_TOKEN")

    def transit_decrypt(self, key, encoded):
        data = json.dumps({"ciphertext": encoded}).encode("utf-8")
        url = "%s/transit/decrypt/%s" % (self.addr, key)
        r = urlopen(url, data)
        data = json.load(r)
        return base64.b64decode(data["plaintext"])
