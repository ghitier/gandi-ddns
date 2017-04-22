import sys
import requests

class ipify:
    def __init__(self):
        self._url = 'https://api.ipify.org'
        self.ip = None

    def get(self, log):
        try:
            self.ip = requests.get(self._url).text
        except:
            log.error('Couldn\'t get public ip address.')
            sys.exit(1)
