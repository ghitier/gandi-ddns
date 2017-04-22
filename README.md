# Gandi Dynamic DNS
#### Dynamically update your Gandi DNS records

## Description
Python(3.5+) script to update DNS records of your domain dynamically using gandi.net's API. Just as no-ip and dyndns you can have a domain that points at your servers's IP address.

This was designed with Synology Diskstations in mind, but could be used as good as anywhere.

Every time te script runs it will get your current external IP from the 'ipify.org' API, then it will check for the IP in the '@' record for the domain (it's '@' by default but you can change that if you want to). Once it has both IPs it will compare what is in the DNS config vs what your IP is, and update the DNS config for the domain as appropriate so that it resolves to your current IP address.

## Installation
### Install modules (if needed)
```bash
sudo python3 -m pip install requests configparser
```

### Configure the script
Edit the **settings.ini** file next to the script:
1. Fill in your domain name
2. Fill your **production** [API Key](https://www.gandi.net/admin/apixml/)

3. *Change the 'A' type which uses the dynamically changing IP (all records with the same IP will get changed as well).*

```ini
[User]
domain =
key =

[DNS]
record = @
```

### Schedule with cron
To check for a new IP every 5 minutes add this to your **/etc/crontab** file:
> Make sure to backup the file before editing.

```text
*/5	*	*	*	*	python3 /<path-to-the-script>/ddns.py
```
**Note all elements before the command to be executed (python3 etc...) are separted by tabs.**
> for detailed information on setting up the crontab file take a look at `man 5 crontab`.

You can start and/or reload the cron config:
```bash
sudo /etc/init.d/cron start
sudo /etc/init.d/cron reload
```

### :sparkles: You are good to go :sparkles:

## Additional information
In case of an event (IP change, failure, etc...), a log file (log.txt) is created next to the script.
