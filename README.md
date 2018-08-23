# sat6-currency
Satellite 6 version of 'spacewalk-report system-currency'

## Requirements
* Python 2.x
* [Requests](http://python-requests.org/)
* [PyYAML](https://pyyaml.org/)

## Usage
Specify server and username on commandline. The script will prompt for password.
```bash
python sat6-currency.py -n satellite.example.com -u admin
```

Load server, username and password from a [Hammer CLI configuration file](https://github.com/theforeman/hammer-cli-foreman/blob/master/doc/configuration.md). Default path is `~/.hammer/cli_config.yml`.
```bash
python sat6-currency.py -c [path/to/config.yml]
```

## Help Output
```
$ python sat6-currency.py
usage: sat6-currency.py [-h] [-a] [-c [CONFIG]] [-n SERVER] [-u USERNAME]
                        [-p PASSWORD] [-s SEARCH]

Satellite 6 version of 'spacewalk-report system-currency'

optional arguments:
  -h, --help            show this help message and exit
  -a, --advanced        Use this flag if you want to divide security errata by
                        severity. Note: this will reduce performance if this
                        script significantly.
  -c [CONFIG], --config [CONFIG]
                        Hammer CLI config file (defaults to
                        ~/.hammer/cli_config.yml
  -n SERVER, --server SERVER
                        Satellite server
  -u USERNAME, --username USERNAME
                        Username to access Satellite
  -p PASSWORD, --password PASSWORD
                        Password to access Satellite. The user will be asked
                        interactively if password is not provided.
  -s SEARCH, --search SEARCH
                        Search string for host.( like
                        ?search=lifecycle_environment=Test
```
