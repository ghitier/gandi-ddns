import os
import sys
import xmlrpc.client
import configparser

import pprint

class gandi:

    def __init__(self):
        self._url = 'https://rpc.gandi.net/xmlrpc/'

    def get_settings(self, log):
        config = configparser.ConfigParser(allow_no_value=True);
        _filename = os.path.dirname(os.path.realpath(__file__)) + '/settings.ini';
        config.read(_filename);
        try:
            self._domain = config['User'].get('domain')
            self._key = config['User'].get('key')
            self._record = config['DNS'].get('record', '@')
        except:
            log.error('Couldn\'t get the settings')
            sys.exit(1)
        if len(self._domain) == 0 or len(self._key) == 0:
            log.error('Domain and API Key need to be set.')
            sys.exit(1)
        if len(self._record) == 0:
            log.warning('DNS Record is unset.')
            self._record = '@'
            config.set('DNS', 'record', '@')
            with open(_filename, 'w') as _file:
                config.write(_file)
                log.warning('DNS Record has been set to "@".')
        
    def connect(self, log):
        self._api = xmlrpc.client.ServerProxy(self._url)
        try:
            _version = self._api.version.info(self._key)
        except:
            log.error('Couldn\'t connect to gandi API.')
            sys.exit(1)

    def get_zoneid(self, log):
        try:
            self._zoneid = self._api.domain.info(self._key, self._domain).get('zone_id')
        except:
            log.error('Couldn\'t access the domain.')
            sys.exit(1)

    def get_ip(self, log):
        records = None
        try:
            self.ip = self._api.domain.zone.record.list(self._key, self._zoneid, 0, {'name' : self._record, 'type' : 'A'})[0].get('value')
        except:
            log.error('Couldn\'t get ip.')
            sys.exit(1)

    def same_ip(self, ip):
        if self.ip != None:
            if self.ip == ip:
                return True
            else:
                return False

    def update_ip(self, log, ip):
        try:
            _version = self._api.domain.zone.version.new(self._key, self._zoneid)
        except:
            log.error('New zone version couldn\'t be created.');
            sys.exit(1)
        # Get record id
        _records = self._api.domain.zone.record.list(self._key, self._zoneid, _version, {'value': self.ip})
        for _record in _records:
            try:
                # Update record
                self._api.domain.zone.record.update(self._key, self._zoneid, _version,
                                                        {'id': _record['id']},
                                                        {
                                                            'name': _record['name'],
                                                            'type': _record['type'],
                                                            'value': ip,
                                                            'ttl': _record['ttl']
                                                        })
            except:
                log.error('Couldn\'t update record' + _record['name'] + '.')
        try:
            # Set the new zone
            self._api.domain.zone.version.set(self._key, self._zoneid, _version)
            self._api.domain.zone.set(self._key, self._domain, self._zoneid)
        except:
            log.error('Couldn\'t set the new zone.')
