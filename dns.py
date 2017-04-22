import sys
import xmlrpc.client

class gandi:

    def __init__(self):
        self._url = 'https://rpc.gandi.net/xmlrpc/'
        self._key = '<YOUR API KEY>'
        self._domain = '<YOUR DOMAIN>'
        self._record = '@'
        self._zoneid = None
        self._api = None
        self.ip = None

    def connect(self, log):
        self._api = xmlrpc.client.ServerProxy(self._url)
        try:
            _version = self._api.version.info(self._key)
        except:
            log.error('Couldn\'t connect to gandi API')
            sys.exit()

    def get_zoneid(self, log):
        try:
            self._zoneid = self._api.domain.info(self._key, self._domain).get('zone_id')
        except:
            log.error('Couldn\'t get zone_id.')
            sys.exit()

    def get_ip(self, log):
        records = None
        try:
            self.ip = self._api.domain.zone.record.list(self._key, self._zoneid, 0, {'name' : self._record, 'type' : 'A'})[0].get('value')
        except:
            log.error('Couldn\'t get ip.')
            sys.exit()

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
            sys.exit()
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
