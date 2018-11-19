import requests


class Ipify:

    @staticmethod
    def get_public_ip():
        try:
            return requests.get('https://api.ipify.org').text
        except (requests.ConnectionError, requests.HTTPError) as e:
            print(e)
        return None
