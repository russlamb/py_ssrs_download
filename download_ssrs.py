import requests, configparser, os 
from requests_ntlm import HttpNtlmAuth

# my imported modules
import date_gen 
import encode_ssrs_url as eu
def get_url(url, username, password, output_file):
    """downlaod SSRS Url using credentials supplied"""
    
    # access the URL
    r = requests.get(url,
                     auth=HttpNtlmAuth(username,password))

    # check request status, output if there was an error
    try:
        r.raise_for_status()
    except Exception as e:
        print('an error occurred downloading the file: %s' % (e))

    # output the request data to a file    
    downloaded_file=open(output_file,'wb')        
    for chunk in r.iter_content(100000):
        downloaded_file.write(chunk)

    return output_file

def download_for_dates(date_list, url, username, password, file_prefix, file_extension):
    """call download function for a list of dates"""

    for i in date_list:
        new_url = eu.modify_url_date(url, i )
        file_name = file_prefix + str(i) + file_extension
        output_file = get_url(new_url, username, password, file_name)
        print("Downloaded: "+output_file)


