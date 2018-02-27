# sat6-currency
Satellite 6 version of 'spacewalk-report system-currency'. 

# Requirements

* python-requests

Tested from RHEL 7.4 against Satellite 6.2.12.

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

# Help Output

~~~
↪ ./sat6-currency.py -h
usage: sat6-currency.py [-h] [-a] -n SERVER -u USERNAME [-p PASSWORD] [-l]
                        [-o ORGANIZATION] [-c CONTENTVIEW] [-e ENVIRONMENT]

Satellite 6 version of 'spacewalk-report system-currency'

optional arguments:
  -h, --help            show this help message and exit
  -a, --advanced        Use this flag if you want to divide security errata by
                        severity. Note: this will reduce performance of this
                        script significantly.
  -n SERVER, --server SERVER
                        Satellite server (defaults to localhost)
  -u USERNAME, --username USERNAME
                        Username to access Satellite
  -p PASSWORD, --password PASSWORD
                        Password to access Satellite. The user will be asked
                        interactively if password is not provided.
  -l, --library         Use this flag to also report on Library Synced Content
                        AND to divide security errata by severity. Note: this
                        will reduce performance of this script significantly.
                        Use with -o, -e and -c options
  -o ORGANIZATION, --organization ORGANIZATION
                        Organization to use when using the '-l' option
  -c CONTENTVIEW, --contentview CONTENTVIEW
                        Content View to use using the '-l' option. Default:
                        Default Organization View
  -e ENVIRONMENT, --environment ENVIRONMENT
                        Environment to use with the '-l' option. Default:
                        Library
~~~
# Notes

* The script will prompt for password if not provided
