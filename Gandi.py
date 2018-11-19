import os
import requests
import configparser
from Record import Record


class Gandi():
    __domain = None
    __api_key = None
    __record = None
    __headers = {}

    def __init__(self):
        self.base_url = 'https://dns.api.gandi.net/api/v5'

    def load_config(self):
        try:
            conf = configparser.ConfigParser(allow_no_value=True);
            conf.read(os.path.dirname(os.path.realpath(__file__)) + '/settings.ini')
            sections = conf.sections()
            if 'User' not in sections or 'DNS' not in sections:
                raise Exception('Missing sections')
            self.__domain = conf['User'].get('domain')
            self.__api_key = conf['User'].get('api_key')
            self.__record = conf['DNS'].get('record', '@')
        except (Exception, configparser.Error) as e:
            print('Unable to load config: ', e)
        self.__headers['X-Api-Key'] = self.__api_key

    def get_record(self):
        try:
            r = requests.get(self.base_url + '/domains/' + self.__domain + '/records/' + self.__record + '/A',
                             headers=self.__headers)
            body = r.json()
            if r.ok:
                return Record(body['rrset_type'], body['rrset_ttl'], body['rrset_name'], body['rrset_values'])
                pass
            else:
                print(body['message'])

        except (requests.ConnectionError, requests.HTTPError) as e:
            print(e)
        return None

    def update_record(self, record):
        try:
            r = requests.put(self.base_url + '/domains/' + self.__domain + '/records/' + record.name + '/' + record.type,
                             json=record.to_dict(), headers=self.__headers)
            if r.ok:
                print("Record " + record.name + " updated.")
            else:
                print("Unable to update " + record.name + ": " + str(r.json()))

        except (requests.ConnectionError, requests.HTTPError) as e:
            print(e)
        return None
