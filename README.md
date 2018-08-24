# sat6-currency
Satellite 6 version of 'spacewalk-report system-currency'. 

# Requirements

* Python 2.x
* [Requests](http://python-requests.org/)
* [PyYAML](https://pyyaml.org/)

Tested from RHEL 7.5 against Satellite 6.3.2.

# Usage
## Basic report
A CSV file is printed on stdout listing each system with details of the number of security, bug and enhancement errata that are available on each host.

~~~
↪ ./sat6Inventory.py -n SERVER -u USERNAME [-p PASSWORD]
~~~

## Advanced report
A CSV file is printed on stdout listing each system with details of the number of security, bug and enhancement errata that are available on each host.  The report takes longer to run, but shows the breakdown of security errata by critical, important, moderate and low severity levels.

~~~
↪ ./sat6Inventory.py -a -n SERVER -u USERNAME [-p PASSWORD] -o 'MyOrganization'
~~~

## Library report
A CSV file is printed on stdout listing each system with details of the number of security, bug and enhancement errata that are both available and applicable to each host.  The report takes longer to run, but shows the breakdown of security errata by critical, important, moderate and low severity levels.  In addition, two CSV files are generated in the working directory listing available and applicable errata for each host.

~~~
↪ ./sat6Inventory.py -l -n SERVER -u USERNAME [-p PASSWORD] -o 'MyOrganization'
~~~

## Configuration file
Server, username and password may be loaded from a [Hammer CLI configuration file](https://github.com/theforeman/hammer-cli-foreman/blob/master/doc/configuration.md) instead of being specified on the command line. The default path for the configuration file is `~/.hammer/cli_config.yml`.
~~~
↪ ./sat6Inventory.py -f [path/to/config.yml]
~~~

# Output
## Scores
A score is shown for each host, based on the number and severity of outstanding errata. Each errata adds the factor for its severity. Simple (default) and advanced mode calculates scores differently.

### Basic report factors

| Severity | Factor |
|----------|-------:|
| security | 8 |
| bug fix | 2 |
| enhancement | 1 |

### Advanced report factors

| Severity | Factor |
|----------|-------:|
| security: critical | 32 |
| security: important | 16 |
| security: moderate | 8 |
| security: low | 4 |
| bug fix | 2 |
| enhancement | 1 |

# Notes

* The script will prompt for password if not provided
