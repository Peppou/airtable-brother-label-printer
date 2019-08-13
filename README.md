This README assumes a Raspbian Stretch (Debian Linux).

## Setup

1. If you don't already have Python 3 installed `sudo apt-get install python3-setuptools python3-pip`
2. Install `brother_ql`: `pip install --upgrade brother_ql`
3. Install pipenv: `pip install --user pipenv`
4. ```cd [REPO_CLONE_DIRECTORY] &&pipenv install```

## Run

```shell
pipenv run python print.py
```