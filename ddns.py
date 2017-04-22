import sys
from log import log
from dns import gandi
from ip import ipify

log = log()
gandi = gandi()
ipify = ipify()

# get the settings
gandi.get_settings(log)

# get external ip address
ipify.get(log)

# connect to gandi API
gandi.connect(log)

# get zone file id in use by gandi DNS
gandi.get_zoneid(log)

# get ip registered by gandi DNS
gandi.get_ip(log)

# check if ip's are the same
if gandi.same_ip(ipify.ip) == False:
    # update ip on gandi DNS server
    log.warning('local (' + ipify.ip + ') and DNS (' + gandi.ip + ') ip addresses are different.')
    gandi.update_ip(log, ipify.ip)
    log.append('updated DNS ip address to ' + log.color['green'] + ipify.ip + log.color['reset'] + '.')
sys.exit(0)
