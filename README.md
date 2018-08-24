# sat6-currency
Satellite 6 version of 'spacewalk-report system-currency'

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
The tables below describe the meaning of each column in the output.

Available errata, also known as installable errata, are those in a server's content view which are able to be installed.
Applicable errata are those in the Library or reference content view which are applicable to the server.

## Basic report

| Column | Description |
|--------|-------------|
| system_id | Server ID |
| org_id | Organization ID which is server registered to |
| name | Name of the server |
| security | Number of security updates available |
| bug | Number of bug fixes available |
| enhancement | Number of enhancements available |
| score | Total system score |
| content_view | Name of the Content View server is registered to |
| content_view_publish_date | Date on which the Content View was published |
| lifecycle_environment | Name of the Lifecycle Environment server is registered to |
| subscription_os_release | |
| os_release | |
| arch | CPU architecture |
| subscription_status | |
| comment | |

## Advanced report

| Column | Description |
|--------|-------------|
| system_id | Server ID |
| org_id | Organization ID which is server registered to |
| name | Name of the server |
| critical | Number of critical security updates available |
| important | Number of important security updates available |
| moderate | Number of moderate importance security updates available |
| low | Number of low importance security updates available |
| bug | Number of bug fixes available |
| enhancement | Number of enhancements available |
| score | Total system score |
| content_view | Name of the Content View server is registered to |
| content_view_publish_date | Date on which the Content View was published |
| lifecycle_environment | Name of the Lifecycle Environment server is registered to |
| subscription_os_release |  |
| os_release |  |
| arch | CPU architecture |
| subscription_status |  |
| comment |  |

## Library report

| Column | Description |
|--------|-------------|
| system_id | Server ID |
| org_id | Organization ID which is server registered to |
| name | Name of the server |
| total_available_security | Total number of security updates available Total number of security updates available |
| critical | Number of critical security updates available |
| important | Number of important security updates available |
| moderate | Number of moderate importance security updates available |
| low | Number of low importance security updates available |
| bug | Number of bug fixes available |
| enhancement | Number of enhancements available |
| score | Total system score |
| total_applicable_security | Total number of security updates applicable |
| applicable_critical | Number of critical security updates applicable |
| applicable_important | Number of important security updates applicable |
| applicable_moderate | Number of moderate security updates applicable |
| applicable_low | Number of low security updates applicable |
| applicable_bug | Number of bug fixes applicable |
| applicable_enhancement | Number of enhancements applicable |
 |applicable_score | Total score of applicable errata |
| content_view | Name of the Content View server is registered to |
| content_view_publish_date | Date on which the Content View was published |
| lifecycle_environment | Name of the Lifecycle Environment server is registered to |
| subscription_os_release |  |
| os_release |  |
| arch | CPU architecture |
| subscription_status |  |
| comment |  |

### Errata report

| Column | Description |
|--------|-------------|
| system_id | Server ID |
| org_id | Organization ID which is server registered to |
| name | Name of the server |
| state | State of the errata: Available or Applicable |
| errata_id | ID of the errata|
| issued | Date the errata was issued |
| updated | Date the errata was updated |
| severity | Errata security severity |
| type | Errata type |
| reboot_suggested | Does the errata suggest rebooting the system after installation |
| title | Title of the errata |
| further_info | URL to errata information web page |

# Scores
A score is shown for each host, based on the number and type of outstanding errata. Each errata adds the factor for its type. The advanced report differentiates security errata based on their severity.

## Basic report factors

| Type/Severity | Factor |
|---------------|-------:|
| Security      |      8 |
| Bug Fix       |      2 |
| Enhancement   |      1 |

## Advanced report factors

| Type/Severity       | Factor |
|---------------------|-------:|
| Security: Critical  |     32 |
| Security: Important |     16 |
| Security: Moderate  |      8 |
| Security: Low       |      4 |
| Bug Fix             |      2 |
| Enhancement         |      1 |

# Notes

* The script will prompt for password if not provided
