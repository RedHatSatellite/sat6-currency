#!/usr/bin/python

import argparse
import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
 
# Satellite specific parameters
url = "https://localhost/"
api = url + "api/"
katello_api = url + "katello/api/"
post_headers = {'content-type': 'application/json'}
ssl_verify=False
username = "admin"
password = "redhat123"
 
parser = argparse.ArgumentParser(description="Satellite 6 version of 'spacewalk-report system-currency'")
parser.add_argument("-a", "--advanced", action="store_true", default=False, help="Use this flag if you want to divide security errata by severity. Note: this will reduce performance if this script significantly.")
args = parser.parse_args()
 
def get_with_json(location, json_data):
    """
    Performs a GET and passes the data to the url location
    """
    try:
        result = requests.get(location,
                            data=json_data,
                            auth=(username, password),
                            verify=ssl_verify,
                            headers=post_headers)
 
    except requests.ConnectionError, e:
        print sys.argv[0] + " Couldn't connect to the API, check connection or url"
        print e
        sys.exit(1)
    return result.json()
 
def simple_currency():
 
    # Print headline
    print "system_id,org_id,name,security,bug,enhancement,score"
 
    # Get all hosts (alter if you have more than 10000 hosts)
    hosts = get_with_json(api + "hosts", json.dumps({"per_page": "10000"}))["results"]
 
    # Multiply factors
    factor_sec = 8
    factor_bug = 2
    factor_enh = 1
 
    for host in hosts:
        # Check if host is registered with subscription-manager (unregistered hosts lack these values and are skipped)
        if "content_facet_attributes" in host and host["content_facet_attributes"]["errata_counts"]:
            
            # Get each number of different kinds of erratas
            errata_count_sec = host["content_facet_attributes"]["errata_counts"]["security"]
            errata_count_bug = host["content_facet_attributes"]["errata_counts"]["bugfix"]
            errata_count_enh = host["content_facet_attributes"]["errata_counts"]["enhancement"]
 
            # Calculate weighted score
            score = errata_count_sec * factor_sec + errata_count_bug * factor_bug + errata_count_enh * factor_enh
 
            # Print result
            print str(host["id"]) + "," + str(host["organization_id"]) + "," + host["name"] + "," + str(errata_count_sec) + "," + str(errata_count_bug) + "," + str(errata_count_enh) + "," + str(score)
 
def advanced_currency():
 
    # Print headline
    print "system_id,org_id,name,critical,important,moderate,low,bug,enhancement,score"
 
    # Get all hosts (if you have more than 10000 hosts, this method will take too long itme)
    hosts = get_with_json(api + "hosts", json.dumps({"per_page": "10000"}))["results"]
 
    # Multiply factors according to "spacewalk-report system-currency"
    factor_cri = 32
    factor_imp = 16
    factor_mod = 8
    factor_low = 4
    factor_bug = 2
    factor_enh = 1
 
    for host in hosts:
 
        # Get all errata for each host
        erratas = get_with_json(api + "hosts/" + str(host["id"]) + "/errata", json.dumps({"per_page": "10000"}))
 
        # Check if host is registered with subscription-manager (unregistered hosts lack these values and are skipped)
        if "results" in erratas:
 
            errata_count_cri = 0
            errata_count_imp = 0
            errata_count_mod = 0
            errata_count_low = 0
            errata_count_enh = 0
            errata_count_bug = 0
 
            # Check if host have any errrata at all
            if "total" in erratas:
 
                # Go through each errata
                for errata in erratas["results"]:
 
                    # If it is a security errata, check the severity
                    if errata["type"] == "security":
                        if errata["severity"] == "Critical": errata_count_cri += 1
                        if errata["severity"] == "Important": errata_count_imp += 1
                        if errata["severity"] == "Moderate": errata_count_mod += 1
                        if errata["severity"] == "Low": errata_count_low += 1
 
                    if errata["type"] == "enhancement": errata_count_enh += 1
                    if errata["type"] == "bugfix": errata_count_bug += 1
 
            # Calculate weighted score
            score = factor_cri * errata_count_cri + factor_imp * errata_count_imp + factor_mod * errata_count_mod + factor_low * errata_count_low + factor_bug * errata_count_bug + factor_enh * errata_count_enh
 
            # Print result
            print str(host["id"]) + "," + str(host["organization_id"]) + "," + host["name"] + "," + str(errata_count_cri) + "," + str(errata_count_imp) + "," + str(errata_count_mod) + "," + str(errata_count_low) + "," + str(errata_count_bug) + "," + str(errata_count_enh) + "," + str(score)
 
 
if __name__ == "__main__":
 
    if args.advanced:
        advanced_currency()
    else:
        simple_currency()

