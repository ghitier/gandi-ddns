#### Dynamically update your Gandi DNS records

## Description
Python(3.5>=) script to update your servers IPv4 address on the DNS records of your domain dynamically using Gandi's API.

The script was designed to work for a Synology Diskstation, but can actually work on any server which has python3 and any task scheduler installed.

Every time the script runs it will get your current external IP and then check for the IP in the '@' record of your domain (it's '@' by default, but you can change that if you want to). Once it has both IPs it will compare them and update your DNS config appropriately in order to resolve the new IP.

## Installation
### Install modules (if needed)
```bash
pip install -r requirements.txt
```
> if you get the setuptools error thingy try `sudo python3 -m pip install -U setuptools` and start over with the module installation.

### Configure the script
Copy the **settings.template.ini** to **settings.ini**, then edit **settings.ini**:
1. Fill in your domain name
2. Fill in your [API Key](https://account.gandi.net/) (go to `Security > ApiKey`)

3. *Change the 'A' type record which uses the dynamically changing IP (all records with the same IP will get changed as well).*

```ini
[User]
domain = example.com
api_key = xXxxxXxxXxXXxXxxXXxXxXxX

[DNS]
record = @
```

### Schedule with cron
To check for a new IP every 5 minutes add this to your **/etc/crontab** file:
> Make sure to backup the file before editing.

```text
*/5	*	*	*	*	python3 /<path-to-the-script>/ddns.py
```
**Note that all elements before the command to be executed (python3 etc...) are separted by tabs.**
> for detailed information on setting up the crontab file take a look at `man 5 crontab`.

You can start and/or reload the cron config:
```bash
sudo /etc/init.d/cron start
sudo /etc/init.d/cron reload
```
> Use `sudo /usr/syno/sbin/synoservicectl --restart crond` on Synology.

### :sparkles: You are good to go :sparkles:
