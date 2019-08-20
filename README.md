airtable-brother-label-printer

This README assumes you are running Raspbian Stretch, though it should largely
work the same for any Debian/Ubuntu setup.

## Setup

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