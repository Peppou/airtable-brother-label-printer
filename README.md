# airtable-brother-label-printer

This README assumes you are running Raspbian Stretch, though it should largely
work the same for any Debian/Ubuntu setup.

## Setup

### Application

1. If you don't already have Python 3 installed:

  ```shell
  sudo apt-get install python3-setuptools python3-pip
  ```

2. Install `brother_ql` Brother printer utility:

  ```shell
  pip install --upgrade brother_ql
  ```

3. Install `pipenv` package management tool:

  ```shell
  pip install --user pipenv
  ```

4. Install packages:

  ```shell
  cd [REPO_CLONE_DIRECTORY] && pipenv install
  ```

### Cron

1. Install postfix to get cron output:

  ```shell
    apt-get install postfix
  ```

2. Edit the `syslog` log configuration to get cron logs at `/var/log/cron.log`. To do so, open `/etc/rsyslog.conf` (you will need to do this as superuser) and uncomment the following line:

  ```
  cron.* /var/log/cron.log
  ```

3. Edit your crons with `crontab -e` and add the following line (replacing missing `<key>` and `<base_id>` values):

  ```
  * * * * * cd /home/pi/airtable-brother-label-printer && AIRTABLE_API_KEY=<key> AIRTABLE_BASE_ID=<base_id>  /home/pi/.local/bin/pipenv run python /home/pi/airtable-brother-label-printer/main.py
  ```

## Run

To test a single run of the job:

```shell
pipenv run python main.py
```

Once you're done testing, you will want to add the script to run on a regular
cron. A recommended interval is every 1 minute, which is more than enough time
for the job to finish, since print jobs are handled asynchronously by the
printer.

See
[here](https://www.cyberciti.biz/faq/how-to-run-cron-job-every-minute-on-linuxunix/)
for how to setup a per minute cron on Linux.