import requests, configparser, os 
from requests_ntlm import HttpNtlmAuth

# my imported modules
import date_gen 
import encode_ssrs_url as eu
from download_ssrs import download_for_dates

def main():
    """example of how to call functions in this module"""
    
    # get parameters from config file
    config = configparser.ConfigParser(interpolation=None)
    config.read(r'config.ini')
    username = config['SSRS']['u']
    password = config['SSRS']['p']
    url = config['SSRS']['url']    

    # generate list of dates
    date_list = date_gen.get_month_end_dates(2016,1)

    # iterate through dates and download url
    download_for_dates(date_list, url, username, password, "ssrs_", ".xls")

if __name__=='__main__':
    main()
