from Gandi import Gandi
from Ipify import Ipify

if __name__ == '__main__':
    gandi = Gandi()
    gandi.load_config()
    record = gandi.get_record()
    if record:
        public_ip = Ipify.get_public_ip()
        if record.value != public_ip:
            print("Public IP has changed to " + public_ip)
            gandi.update_record(record.update_ip(public_ip))
        else:
            print("IP is still " + record.value)
